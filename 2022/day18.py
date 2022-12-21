from collections import deque
with open(0) as f:
	content = f.read().strip()
	lines = content.splitlines()
	# lines.append("")

grid = {}

for line in lines:
    x,y,z = map(int, line.split(","))
    
    grid[(x,y,z)] = 1

from collections import defaultdict
ans = 0
mx=my=mz=float("inf")
Mx=My=Mz= 0
delta = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]
cubes = defaultdict(lambda: 0)
empty = []
for x,y,z in grid:
    mx = min(mx, x)
    my = min(my, y)
    mz = min(mz, z)
    Mx = max(Mx, x)
    My = max(My, y)
    Mz = max(Mz, z)
    for i,j,k in delta:
        if (x+i, y+j, z+k) not in grid:
            ans += 1
            cubes[(x+i, y+j, z+k)] += 1
            empty.append((x+i, y+j, z+k))

print(ans)
import sys
sys.setrecursionlimit(int(1e6))
def dfs(x, y, z, vis):
    ans = 1
    vis.add((x,y,z))
    for i,j,k in delta:
        if (x+i, y+j, z+k) in vis or (x+i, y+j, z+k) in grid: continue
        if  mx > x+i or x+i > Mx or my > y+j or y+j > My or mz > z+k or z+k > Mz:
            return 0
        # print(x,y,z)
        ans = min(ans, dfs(x+i, y+j, z+k, vis))
    return ans
    
    
for x,y,z in empty:
    if  mx > x or x > Mx or my > y or y > My or mz > z or z > Mz:
        continue
    ans -= dfs(x,y,z, set())

print(ans)