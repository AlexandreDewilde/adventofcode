from collections import deque, defaultdict

with open(0) as f:
	content = f.read()
	lines = content.splitlines()
    
grid = defaultdict(lambda: ".")
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        grid[(i,j)] = char

def check_neigh(x,y):
    pos = set()
    for i in range(-1,2):
        for j in range(-1,2):
            if i == 0 == j: continue
            
            if grid[(x+i, y+j)] == "#":
                pos.add((i,j))
    return pos

directions = deque([({(-1,-1), (-1,1), (-1,0)}, (-1,0)), ({(1,1), (1,0), (1,-1)}, (1,0)), ({(-1,-1), (0,-1), (1,-1)}, (0,-1)), ({(1,1), (0,1), (-1,1)}, (0,1))])
for round_ in range(10000):
    moved = False
    to = {}
    for i, j in grid.copy():
        if grid[(i,j)] == ".":
            continue
        neigh = check_neigh(i,j)
        # print(neigh)
        if not neigh:
            continue
        for d in directions:
            if not (d[0] & neigh):
                to[(i+d[1][0], j+d[1][1])] = to.get((i+d[1][0], j+d[1][1]), []) + [(i,j)]
                break
    # print(to_go)
    for k, val in to.items():
        if len(val) > 1:
            continue
        grid[k] = "#"
        grid[val[0]] = "."
        moved = True
    if not moved:
        print(round_+1)
        break
    directions.append(directions.popleft())
# For part 1
my = mx = float('inf')
My = Mx = float("-inf")
for i,j in grid:
    if grid.get((i,j)) == "#":
        my = min(my, j)
        mx = min(mx, i)
        My = max(My, j)
        Mx = max(Mx, i)
ans = 0
for i in range(mx, Mx+1):
    for j in range(my, My+1):
        ans += grid.get((i,j)) != "#"
# for i in range(-20, 20):
#     print("".join(grid[(i,j)] for j in range(-20,20)))
# print(ans)