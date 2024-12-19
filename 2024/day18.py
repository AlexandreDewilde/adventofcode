from aoctools import *
from functools import cmp_to_key
import random
from collections import deque
import heapq

aocd = AOCD(2024, 18)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """ """

WIDTH = 71

grid = [["."]*WIDTH for _ in range(WIDTH)]

def sim(nb):
    for x, y in list(map(int, line.split(",")) for line in puzzle_input.splitlines())[:nb]:
        grid[y][x] = "#"

    q = deque([(0, 0)])
    dst = [[float("inf")]*WIDTH for _ in range(WIDTH)]
    dst[0][0] = 0
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < WIDTH and 0 <= ny < WIDTH and grid[ny][nx] == "." and dst[ny][nx] == float("inf"):
                dst[ny][nx] = dst[y][x] + 1
                q.append((nx, ny))
    return dst[WIDTH-1][WIDTH-1] == float("inf")

for i in range(len(puzzle_input.splitlines())):
    if sim(i):
        ans = puzzle_input.splitlines()[i-1]
        break
print(ans)
input()
aocd.p1(ans)
input()
aocd.p2(ans)