from collections import deque
with open(0) as f:
	content = f.read().strip()
	lines = content.splitlines()
	# lines.append("")


rocks_str = """####

.#.
###
.#.

..#
..#
###

#
#
#
#

##
##

"""

rocks = []
current = []
for line in rocks_str.splitlines():
	if line in {"", "\n"}:
		rocks.append(current)
		current = []
	else:
		current.append(list(line))

from collections import defaultdict
grid = defaultdict(lambda: '.')
def can_move(coords, symbol):
	dx = (-1 if symbol == "<" else 1) if symbol in "<>" else 0
	dy = -1 if symbol == "down" else 0
	for i, coord in enumerate(coords):
		x,y = coord
		grid[(x,y)] = '.'
	poss = True
	for x, y in coords:
		if not (0<= x + dx < 7 and 0<= y + dy and grid[(x+dx,y+dy)] == '.'):
			poss = False
			break
	for i, coord in enumerate(coords):
		x,y = coord
		grid[(x,y)] = '#'
	return poss
	
def move(coords, symbol):
	dx = (-1 if symbol == "<" else 1) if symbol in "<>" else 0
	dy = -1 if symbol == "down" else 0
	for i, coord in enumerate(coords):
		x,y = coord
		grid[(x,y)] = '.'
	for i, coord in enumerate(coords):
		x,y = coord
		x += dx
		y += dy
		grid[(x,y)] = '#'
		coords[i] = (x,y)

highest = -1

def create_new_grid():
	deepest = highest
	for i in range(7):
		j = highest
		while j >= 0:
			deepest = min(deepest, j)
			if grid.get((i,j)) == "#":
				break
			j -= 1
	subgrid = defaultdict(lambda: '.')
	for i in range(7):
		for j in range(highest, deepest-1,-1):
			res = grid.get((i,j))
			if res == "#":
				subgrid[(i,j)] = "#"
	return subgrid
nb = 1514285714288 *10

def to_string():
	# l = []
	s = ""
	for j in range(highest, highest-5, -1):
		for i in range(7):
			s += grid[(i,j)]
		# l.append(s)
	return s

def display():
	for jj in range(highest, -1,-1):
		s = ""
		for ii in range(0, 7):
			s += grid.get((ii,jj), '.')
		print(s)
	print()
j = 0

pattern = {}
res = []
for i in (range(100000)):
	coords = []
	cx = 2
	cy = highest + 3 + len(rocks[i%len(rocks)])
	prev_highest = highest
	highest = cy
	prev_j = j
	for l in rocks[i%len(rocks)]:
		cx = 2
		for ch in l:
			if ch == "#":
				grid[(cx,cy)] = "#"
				coords.append((cx,cy))
			cx += 1
		cy -= 1

	while True:
		moved = False
		if can_move(coords, content[j%len(content)]):
			move(coords, content[j%len(content)])
			moved = True
		j += 1
		if can_move(coords, "down"):
			move(coords, "down")
			highest -= 1
		else: 
			break
	highest = max(highest, prev_highest)
	res.append(highest)
	if highest < 5:
		continue
	if (to_string(), j%len(content), i%len(rocks)) in pattern:
		pattern[(to_string(), j%len(content), i%len(rocks))].append((highest, i))
		if len(pattern[(to_string(), j%len(content), i%len(rocks))]) >= 3:
			ps = pattern[(to_string(), j%len(content), i%len(rocks))]
			heigh =  ps[1][0] - ps[0][0]
			c_l = ps[1][1] - ps[0][1]
			print(heigh, c_l)
			ans = ((1000000000000 - ps[0][1]) // c_l)*heigh + res[ps[0][1] + (1000000000000 - ps[0][1]) % c_l]
			print(ans)
			# print(j%len(content), i%len(rocks), pattern[(to_string(), j%len(content), i%len(rocks))],i)
			break
	else:
		pattern[(to_string(), j%len(content), i%len(rocks))] = [(highest, i)]
	
print(highest+1)
