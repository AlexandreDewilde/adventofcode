from aoctools import *
from functools import cmp_to_key
from collections import deque
import heapq

aocd = AOCD(2024, 16)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """#################
# #...#...#...#..E#
# #.#.#.#.#.#.#.#.#
# #.#.#.#...#...#.#
# #.#.#.#.###.#.#.#
# #...#.#.#.....#.#
# #.#.#.#.#.#####.#
# #.#...#.#.#.....#
# #.#.#####.#.###.#
# #.#.#.......#...#
# #.#.###.#####.###
# #.#.#...#.....#.#
# #.#.#.#####.###.#
# #.#.#.........#.#
# #.#.#.#########.#
# #S#.............#
# #################"""

grid = [list(line) for line in puzzle_input.splitlines()]
start = None
end = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            grid[i][j] = "."
            start = (i, j)

        if grid[i][j] == "E":
            grid[i][j] = "."
            end = (i, j)

def dij(start, start_dir=1):
    pq = [(0, start_dir, *start)]

    dst = [[[float("inf")]*4 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dst[start[0]][start[1]][start_dir] = 0

    while pq:
        d, dir, x, y = heapq.heappop(pq)
        if d > dst[x][y][dir]:
            continue

        for i, (dx, dy) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] != "#":
                turn = 1000 if dir != i else 0
                turn += 1000 if abs((dir - i)) == 2 else 0
                new_d = dst[x][y][dir] + 1 + turn
                if new_d < dst[nx][ny][i]:
                    dst[nx][ny][i] = new_d
                    heapq.heappush(pq, (new_d, i, nx, ny))
    return dst

bests = [[False] * len(grid[0]) for _ in range(len(grid))]
dst = dij(start)

for i in range(4):
    dst2 = dij(end, i)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            for k in range(4):
                for k2 in range(4):
                    turn = 1000 if abs(k - k2) != 2 else 0
                    turn += 1000 if k - k2 == 0 else 0
                    if turn + dst[i][j][k] + dst2[i][j][k2] == min(dst[end[0]][end[1]]):
                        bests[i][j] = True

ans = sum(bests[i][j] for i in range(len(bests)) for j in range(len(bests[i])))

for i, line in enumerate(grid):
    line = "".join(("O" if bests[i][j] else el) for j, el in enumerate(line))
    print(line)
# print(dst)
# ans = min(dst[end[0]][end[1]])
print(ans)
input()
aocd.p1(ans)
input()
aocd.p2(ans)