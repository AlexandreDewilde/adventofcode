from aoctools import *
from functools import cmp_to_key
import random
from collections import deque
import heapq
import sys
sys.setrecursionlimit(10**6)

aocd = AOCD(2024, 20)
puzzle_input = open('input').read().strip()
ans = 0

# puzzle_input = """###############
# #...#...#.....#
# #.#.#.#.#.###.#
# #S#...#.#.#...#
# #######.#.#.###
# #######.#.#...#
# #######.#.###.#
# ###..E#...#...#
# ###.#######.###
# #...###...#...#
# #.#####.#.###.#
# #.#...#.#.#...#
# #.#.#.#.#.#.###
# #...#...#...###
# ###############"""

grid = [list(x) for x in puzzle_input.splitlines()]

for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == 'S':
            start = (i, j)
            grid[i][j] = '.'
        if grid[i][j] == 'E':
            end = (i, j)
            grid[i][j] = '.'

def bfs(start):
    dst = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dst[start[0]][start[1]] = 0
    q = deque([start])
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#' and dst[nx][ny] == float('inf'):
                dst[nx][ny] = dst[x][y] + 1
                q.append((nx, ny))
    return dst

dst1 = bfs(start)
dst2 = bfs(end)

def poss(i, j):
    shortest = float('inf')
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = i + dx, j + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != '#':
            for dxx, dyy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if dx == dxx and dy == dyy:
                    continue
                nxx, nyy = i + dxx, j + dyy
                if 0 <= nxx < len(grid) and 0 <= nyy < len(grid[0]) and grid[nxx][nyy] != '#':
                    shortest = min(shortest, dst1[nx][ny] + dst2[nxx][nyy] + 1)
    return shortest

def poss2(start):
    dst = [[float('inf') for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dst[start[0]][start[1]] = 0
    q = deque([start])
    ret = []
    while q:
        x, y = q.popleft()
        if dst[x][y] >= 20:
            continue
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '.' and dst[nx][ny] == float('inf'):
                dst[nx][ny] = dst[x][y] + 1
                ret.append(((nx, ny), dst[nx][ny]))
                q.append((nx, ny))
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == '#' and dst[nx][ny] == float('inf'):
                dst[nx][ny] = dst[x][y] + 1
                q.append((nx, ny))
    return ret

ans = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == '.':
            for (ii, jj), d in poss2((i, j)):
                if dst1[i][j] + dst2[ii][jj] + d + 100 <= dst1[end[0]][end[1]]:
                    ans += 1
        print(i, j, ans)
# MORE = 100
# visited = set()
# done_cheat = set()
# try_cheat = {}
# def dfs(i, j, current, still, start_cheat=None, done=None):
#     if done and done in done_cheat:
#         return 0
#     if done and current + MORE + dst2[i][j] <= dst1[end[0]][end[1]]:
#         done_cheat.add(done)
#         # print(1)
#         return 1

#     if i == end[0] and j == end[1]:
#         # print(current, path)
#         if (current + MORE <= dst1[end[0]][end[1]]) and done not in done_cheat:
#             done_cheat.add(done)
#             # print(2)
#             return 1
#         return 0

#     if still == 0 and current + dst2[i][j] + MORE > dst1[end[0]][end[1]]:
#         return 0

#     if abs(i - end[0]) + abs(j - end[1]) + current + MORE > dst1[end[0]][end[1]]:
#         return 0

#     if current + MORE > dst1[end[0]][end[1]]:
#         return 0

#     if (i, j) in visited:
#         return 0

#     visited.add((i, j))

#     ret = 0

#     for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#         nx, ny = i + dx, j + dy
#         if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
#             if grid[nx][ny] != '#':
#                 if start_cheat:
#                     # if (start_cheat, (i, j)) not in done_cheat:
#                     #     done_cheat.add((start_cheat, (i, j)))
#                     if try_cheat.get((start_cheat, (nx, ny)), float("inf")) > current + 1:
#                         ret += dfs(nx, ny, current + 1, 0 if still < 20 else 20, None, (start_cheat, (nx, ny)))
#                         try_cheat[(start_cheat, (nx, ny))] = current + 1
#                 else:
#                     ret += dfs(nx, ny, current + 1, 0 if still < 20 else 20, None, done)
#             if still > 1 and grid[nx][ny] == '#':
#                 ret += dfs(nx, ny, current + 1, still - 1, (i, j) if not start_cheat else start_cheat, done)

#     visited.remove((i, j))
#     return ret

# ans = dfs(start[0], start[1], 0, 20)
print(ans)
input()
aocd.p1(ans)
input()
aocd.p2(ans)