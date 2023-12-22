import requests
import os
day = "22"
year = "2023"

def get_example(day,offset=0):
	req = requests.get(f'https://adventofcode.com/{year}/day/{day}', headers={'cookie':'session='+os.environ["SESSION_AOC"]})
	return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
	input(f'You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort.')
	data = {
	  'level': str(level),
	  'answer': str(answer)
	}

	response = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', headers={'cookie':'session='+os.environ["SESSION_AOC"]}, data=data)
	if 'You gave an answer too recently' in response.text:
		print('VERDICT : TOO MANY REQUESTS')
	elif 'not the right answer' in response.text:
		if 'too low' in response.text:
			print('VERDICT : WRONG (TOO LOW)')
		elif 'too high' in response.text:
			print('VERDICT : WRONG (TOO HIGH)')
		else:
			print('VERDICT : WRONG (UNKNOWN)')
	elif 'seem to be solving the right level.' in response.text:
		print('VERDICT : INVALID LEVEL')
	else:
		print('VERDICT : OK !')


content = ""
file = "sample.txt"
file = "input.txt"

if not os.path.exists(file):
	cookies = {"session": os.environ["SESSION_AOC"]}
	content = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
		cookies=cookies,
		headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0"}
	).text
	with open("input.txt", "w") as f:
		f.write(content)
else:
	with open(file) as f:
		content = f.read()

from functools import cmp_to_key
# content = get_example(day, 0)

ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]

coords = []
for line in lines:
	c1, c2 = line.split("~")
	coords.append((list(map(int, c1.split(","))), list(map(int, c2.split(",")))))
plane = {}

def cmp(a,b):
	z1 = min(a[0][2], a[1][2])
	z2 = min(b[0][2], b[1][2])
	if z1 != z2:
		return z1 - z2
	x1 = min(a[0][0], a[1][0])
	x2 = min(b[0][0], b[1][0])
	return x1 - x2

coords.sort(key=cmp_to_key(cmp))

def getLine(start, end):
	if start[0] != end[0]:
		if start[0] > end[0]:
			start, end = end, start
		return [(i, start[1], start[2]) for i in range(start[0], end[0]+1)]
	if start[1] != end[1]:
		if start[1] > end[1]:
			start, end = end, start
		return [(start[0], i, start[2]) for i in range(start[1], end[1]+1)]
	if start[2] > end[2]:
		start, end= end, start
	return [(start[0], start[1], j) for j in range(start[2], end[2]+1)]

def can(start, end):
	line = getLine((start[0], start[1], start[2] - 1), (end[0], end[1], end[2] - 1))
	for x, y, z in line:
		if z < 1 or plane.get((x,y,z)):
			return False
	return True

def add_to_plan(start, end, idx):
	for x, y, z in getLine(start, end):
		plane[(x,y,z)] = idx

for i in range(len(coords)):
	start, end = coords[i]
	while can(start, end):
		start[2] -= 1
		end[2] -= 1

	add_to_plan(start, end, i + 1)

cannot = set()

def check(coord):
	used = set()
	for x, y, z in getLine(*coord):
		idx = plane.get((x,y,z-1))
		if idx:
			used.add(idx)
	idx = plane.get(tuple(coord[0]))

	if idx in used:
		used.remove(idx)
	return used if len(used) <= 1 else set()

def down(idx):
	coord = coords[idx]
	used = set()
	for x, y, z in getLine(*coord):
		idx = plane.get((x,y,z-1))
		if idx:
			used.add(idx)
	idx = plane.get(tuple(coord[0]))

	if idx in used:
		used.remove(idx)
	return used

def up(idx):
	coord = coords[idx]
	used = set()
	for x, y, z in getLine(*coord):
		idx = plane.get((x,y,z+1))
		if idx:
			used.add(idx)
	idx = plane.get(tuple(coord[0]))

	if idx in used:
		used.remove(idx)
	return used

for i in range(len(coords)):
	cannot |= (check(coords[i]))

def compute(idx, broke):
	if idx in broke:
		return
	broke.add(idx)
	for i in up(idx-1):
		print(i)
		if min(coords[i-1][0][2], coords[i-1][1][2]) == 1:
			continue
		for j in down(i-1):
			if j not in broke:
				break
		else:
			compute(i, broke)


ans = 0
for i in range(len(coords)):
	if i+1 in cannot or True:
		broke = set()
		res = compute(i, broke)
		ans += len(broke) - 1
		print(broke)
# ans = len(coords) - len(cannot)
print(ans)
# submit(day, 1, ans)
# submit(day, 2, ans)