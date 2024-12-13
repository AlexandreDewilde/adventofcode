from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 6)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#..."""

grid = [list(line) for line in puzzle_input.splitlines()]

start = (0, 0)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "^":
            start = (i, j)
            break

current = start
vis = set()
vis.add(current)
dir = 0
while 0 <= current[0] < len(grid) and 0 <= current[1] < len(grid[0]):
    nxt = (current[0] + [-1, 0, 1, 0][dir], current[1] + [0, 1, 0, -1][dir])
    if not (0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0])):
        break
    if grid[nxt[0]][nxt[1]] == "#":
        dir = (dir + 1) % 4
        continue
    current = nxt
    vis.add(nxt)
for i in range(len(grid)):
    for j in range(len(grid[i])):
        prev = grid[i][j]
        grid[i][j] = "#"
        current = start
        vis = set()
        dir = 0
        while (*current, dir) not in vis:
            vis.add((*current, dir))
            nxt = (current[0] + [-1, 0, 1, 0][dir], current[1] + [0, 1, 0, -1][dir])
            if not (0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0])):
                break
            if grid[nxt[0]][nxt[1]] == "#":
                dir = (dir + 1) % 4
                continue
            current = nxt
        ans += int((0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0])))
        grid[i][j] = prev
# import sys
# sys.setrecursionlimit(10**6)
# vis = set()
# def dfs(x, y, dir, used):
#     if (x, y, dir) in vis:
#         return 1
#     nxt = (x + [-1, 0, 1, 0][dir], y + [0, 1, 0, -1][dir])
#     if not (0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0])):
#         return 0

#     vis.add((x, y, dir))
#     ret = 0
#     if grid[nxt[0]][nxt[1]] == "#" or (used and used == nxt):
#         ret = dfs(x, y, (dir + 1) % 4, used)
#     else:
#         ret = dfs(nxt[0], nxt[1], dir, used)
#         if not used and start != (nxt[0], nxt[1]) and all((nxt[0], nxt[1], i) not in vis for i in range(4)):
#             ret += dfs(x, y, (dir + 1) % 4, (nxt[0], nxt[1]))

#     vis.remove((x, y, dir))
#     return ret
# ans = dfs(start[0], start[1], 0, 0)
print(ans)
# ans = len(vis)
# print(ans)
# input()
# aocd.p1(ans)
# input()
# aocd.p2(ans)