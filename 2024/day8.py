from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 8)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............"""

puzzle_input = puzzle_input.split("\n")
mappings = {}
grid = [[0 for i in range(len(puzzle_input[0]))] for j in range(len(puzzle_input))]
for i in range(0, len(puzzle_input)):
    for j in range(len(puzzle_input)):
        if puzzle_input[i][j] != ".":
            mappings[puzzle_input[i][j]] = mappings.get(puzzle_input[i][j], []) + [(i, j)]


for el, val in mappings.items():
    for x, y in val:
        for xx, yy in val:
            if x == xx and y == yy:
                continue
            abse = ((x - xx), (y - yy))
            poss = [(x - abse[0], y - abse[1]), (x + abse[0], y - abse[1]), (x + abse[0], y + abse[1]), (x - abse[0], y + abse[1])]
            for it, (i, j) in enumerate(poss):
                # print(i, j, x, y, xx, yy, 2 * abs(i - x) + 2 * abs(j - y), abs(i - xx) + abs(j - yy))
                if not (2 * abs(i - x) + 2 * abs(j - y) == abs(i - xx) + abs(j - yy)):
                    continue
                grid[x][y] = 1
                while 0 <= i < len(grid) and 0 <= j < len(grid[0]):
                    grid[i][j] = 1
                    i, j = poss = [(i - abse[0], j - abse[1]), (i + abse[0], j - abse[1]), (i + abse[0], j + abse[1]), (i - abse[0], j + abse[1])][it]
            # exit()
print(grid)
ans = sum([sum(line) for line in grid])
print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)