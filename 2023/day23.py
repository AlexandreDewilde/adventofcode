content = open("input.txt").read()

ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]

start = None

for j in range(len(grid[0])):
	if grid[0][j] == ".":
		start = (0, j)

best = [0]
stack = [(start, 0, (-1,-1))]
done = set()
bests = {}
while stack:
	if stack[-1][0] == "bests":
		_, pos, prev = stack.pop()
		bests[pos] = prev
		continue
	if stack[-1][0] == "remove":
		done.remove(stack.pop()[1])
		continue
	(i, j), d, par = stack.pop()
	done.add((i,j))
	if bests.get((i, j), -1) >= d:
		continue
	stack.append(("bests", (i,j), bests.get((i,j), -1)))
	bests[(i,j)] = d
	if i == len(grid) - 1:
		best[0] = max(best[0], d)
		print(best[0])
		continue

	for ii, jj in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
		if 0 <= ii < len(grid) and 0 <= jj < len(grid[0]) and (ii, jj) not in done and grid[ii][jj] != "#":
			stack.append(("remove", (ii, jj)))
			stack.append(((ii, jj), d + 1, (i, j)))

print(best)