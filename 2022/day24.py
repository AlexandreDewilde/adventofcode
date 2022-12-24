from collections import deque, defaultdict

with open(0) as f:
	content = f.read()
	lines = content.splitlines()
    
n = len(lines)
m = len(lines[0])
grid = [[[] for _ in range(m)] for _ in range(n)]
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char not in "#.":
            grid[i][j] = [char]

    

grids = [grid]
for r in range(1000):
    new_grid = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(1,n-1):
        for j in range(1,m-1):
            for blizzard in grid[i][j]:
                if blizzard == ">":
                    if j + 1 < m - 1:
                        new_grid[i][j+1].append(blizzard)
                    else:
                        new_grid[i][1].append(blizzard)
                elif blizzard == "<":
                    if j - 1 > 0:
                        new_grid[i][j-1].append(blizzard)
                    else:
                        new_grid[i][m-2].append(blizzard)
                elif blizzard == "^":
                    if i - 1 > 0:
                        new_grid[i-1][j].append(blizzard)
                    else:
                        new_grid[n-2][j].append(blizzard)
                elif blizzard == "v":
                    if i+1 < n - 1:
                        new_grid[i+1][j].append(blizzard)
                    else:
                        new_grid[1][j].append(blizzard)
    
    grid = new_grid
    grids.append(grid)
    
delta = [(0,1), (0,-1), (1,0), (-1,0)]
start = (0,1)
reach = (n-1, m-2)
vis = set()
q = deque([(0, start)])
# for i in range(n):
#     print("".join(char[0] if char else "." for char in grids[1][i]))

while q:
    round_, start = q.popleft()
    if round_ >= len(grids) - 1:
        break
    if (round_, start) in vis:
        continue
    vis.add((round_, start))
    for dx, dy in delta:
        if start[0] + dx == reach[0] and start[1] + dy == reach[1]:
            # print(new_grid)
            print(round_+1, start)

            
            q = deque([(round_+1, reach)])
            if reach == (n-1, m-2):
                reach = (1,1)
            else:
                reach = (n-1, m-2)
            vis = set()
        if (0 < start[0] + dx < n-1 and 0 < start[1] +dy < m-1
            and not grids[round_+1][start[0]+dx][start[1]+dy]):
            q.append((round_ + 1, (start[0]+dx, start[1]+dy)))
    
    else:
        if not grids[round_+1][start[0]][start[1]] :
            q.append((round_ + 1, start))
        continue
