grid = open("input").read().splitlines()

start = grid[0].index("S")

beams = [start]
ans = 0
# for i in range(1, len(grid)):
#     new_beams = set()
#     while beams:
#         c = beams.pop()
#         if grid[i][c] == "^":
#             if i + 1 < len(grid) and c and grid[i + 1][c - 1] != "^":
#                 new_beams.add(c - 1)
#             if (
#                 i + 1 < len(grid)
#                 and c + 1 <= len(grid[i + 1])
#                 and grid[i + 1][c + 1] != "^"
#             ):
#                 new_beams.add(c + 1)
#             ans += 1
#         else:
#             new_beams.add(c)
#     beams = list(new_beams)

from functools import cache


@cache
def dp(i, c):
    if i == len(grid):
        return 1
    if grid[i][c] == "^":
        res = 0
        if i + 1 < len(grid) and c and grid[i + 1][c - 1] != "^":
            res += dp(i + 1, c - 1)
        if (
            i + 1 < len(grid)
            and c + 1 <= len(grid[i + 1])
            and grid[i + 1][c + 1] != "^"
        ):
            res += dp(i + 1, c + 1)
        return res
    else:
        return dp(i + 1, c)


print(dp(0, start))
