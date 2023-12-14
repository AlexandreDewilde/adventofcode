with open("input.txt") as f:
    content = f.read()

ans = 0

def check(j, grid):
    start = j
    end = j + 1
    tot = 0
    while start >= 0 and end < len(grid[0]):
        for i in range(len(grid)):
            if grid[i][start] != grid[i][end]:
                tot += 1
        start -= 1
        end += 1
    return tot
def check2(i, grid):
    start = i
    end = i + 1
    tot = 0
    while start >= 0 and end < len(grid):
        for j in range(len(grid[0])):
            if grid[start][j] != grid[end][j]:
                tot += 1
        start -= 1
        end += 1
    return tot
for block in content.split("\n\n"):
    grid = block.split()
    for mid in range(len(grid[0])-1):
        if check(mid, grid) == 1:
            print(mid)
            ans += mid + 1
    for mid in range(len(grid)-1):
        if check2(mid, grid) == 1:
            print(mid)
            ans += (mid+1) * 100
print(ans)