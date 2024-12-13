from aoctools import *

aocd = AOCD(2024, 4)
puzzle_input = aocd.as_str
ans = 0

grid = puzzle_input.splitlines()

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         if "XMAS" == grid[i][j:j+4] or "XMAS" == grid[i][j:j+4][::-1]:
#             ans += 1

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         word = ""
#         for k in range(4):
#             if i+k < len(grid):
#                 word += grid[i+k][j]
#         if "XMAS" == word or "XMAS" == word[::-1]:
#             ans += 1

# for i in range(len(grid)):
#     for j in range(len(grid[i])):
#         word = ""
#         for k in range(4):
#             if i+k < len(grid) and j+k < len(grid[i]):
#                 word += grid[i+k][j+k]
#         if "XMAS" == word or "XMAS" == word[::-1]:
#             ans += 1
#         word = ""
#         for k in range(4):
#             if i+k < len(grid) and j-k >= 0:
#                 word += grid[i+k][j-k]
#         if "XMAS" == word or "XMAS" == word[::-1]:
            # ans += 1


for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] != "A":
            continue
        could_be = True
        if not((grid[i-1][j-1] == "M" and grid[i+1][j+1] == "S") or (grid[i-1][j-1] == "S" and grid[i+1][j+1] == "M")):
            could_be = False
        if not ((grid[i-1][j+1] == "M" and grid[i+1][j-1] == "S") or (grid[i-1][j+1] == "S" and grid[i+1][j-1] == "M")):
            could_be = False
        ans += could_be


print(ans)
input()
# aocd.p1(ans)
aocd.p2(ans)