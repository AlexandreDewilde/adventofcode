from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 10)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

grid = [list(map(int, line)) for line in puzzle_input.split("\n")]
def dfs(current,x,y, done = set()):
    if current == 9:
        # if (x,y) in done:
        #     return 0
        done.add((x,y))
        return 1
    ret = 0
    for adj in [(0,1),(0,-1),(1,0),(-1,0)]:
        dx,dy = adj
        if 0 <= x+dx < len(grid) and 0 <= y+dy < len(grid[0]) and grid[x+dx][y+dy] == current + 1:
            ret += dfs(current+1,x+dx,y+dy, done)

    return ret

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 0:
            ans += dfs(0,i,j, set())
            # print(dfs(0,i,j, set()))
print(ans)
input()
# aocd.p1(ans)
# input()
#
aocd.p2(ans)