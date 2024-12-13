from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 12)
puzzle_input = aocd.as_str
ans = 0



# puzzle_input = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE"""
grid = [list(line) for line in puzzle_input.splitlines()]

vis = set()

def dfs(x, y):
    if (x, y) in vis:
        return set(), 0
    vis.add((x, y))
    area = 0
    per = set([(x, y)])
    for xx, yy in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
        if 0 <= xx < len(grid) and 0 <= yy < len(grid[0]) and grid[xx][yy] == grid[x][y]:
            np, na = dfs(xx, yy)
            per |= np
            area += na


    return per, area + 1

def cnt(els, debug=False):
    ret = 0
    for i in range(len(grid)):
        broke = True
        for j in range(len(grid[i])):
            if (i, j) not in els:
                broke = True
                continue
            if (i - 1, j) not in els:
                if broke:
                    ret += 1
                broke = False
            if (i-1, j) in els:
                broke = True
    if debug:
        print(ret)
    for i in range(len(grid) - 1, -1, -1):
        broke = True
        for j in range(len(grid[i])):
            if (i, j) not in els:
                broke = True
                continue
            if (i + 1, j) not in els:
                if broke:
                    ret += 1
                broke = False
            if (i+1, j) in els:
                broke = True
    if debug:
        print(ret)
    for j in range(len(grid[0])):
        broke = True
        for i in range(len(grid)):
            if (i, j) not in els:
                broke = True
                continue
            if (i, j - 1) not in els:
                if broke:
                    ret += 1
                broke = False
            if (i, j-1) in els:
                broke = True
    if debug:
        print(ret)
    for j in range(len(grid[0]) - 1, -1, -1):
        broke = True
        for i in range(len(grid)):
            if (i, j) not in els:
                broke = True
                continue
            if (i, j + 1) not in els:
                if broke:
                    ret += 1
                broke = False
            if (i, j+1) in els:
                broke = True
    return ret

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if (i, j) not in vis:
            per, area = dfs(i, j)
            ans += area * cnt(per)
print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)