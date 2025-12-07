grid = open("input").read().split("\n")
grid = [list(row) for row in grid]

ans = 0

while True:
    new_grid = [list(row) for row in grid]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] != "@":
                continue
            total = 0
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if ii == 0 and jj == 0:
                        continue
                    ni, nj = ii + i, jj + j
                    if (
                        0 <= ni < len(grid)
                        and 0 <= nj < len(grid[i])
                        and grid[ni][nj] == "@"
                    ):
                        total += 1
                        # print(ni, nj)
            # print(i, j, total)
            if total < 4:
                new_grid[i][j] = "."
                ans += 1
    grid = new_grid
    print(ans)
