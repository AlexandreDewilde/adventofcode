content = open("input.txt").read()

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
