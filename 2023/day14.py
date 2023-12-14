with open("input.txt") as f:
    content = f.read()

lines = content.splitlines()

lines = [list(line) for line in lines]

def dir():
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] != "O":
                continue
            ii = i - 1
            while ii >= 0 and lines[ii][j] == ".":
                lines[ii][j] = "O"
                lines[ii+1][j] = "."
                ii -= 1
    for j in range(len(lines[0])):
        for i in range(len(lines)):
            if lines[i][j] != "O":
                continue
            jj = j - 1
            while jj >= 0 and lines[i][jj] == ".":
                lines[i][jj] = "O"
                lines[i][jj+1] = "."
                jj -= 1

    for i in range(len(lines)-1,-1,-1):
        for j in range(len(lines[i])):
            if lines[i][j] != "O":
                continue
            ii = i + 1
            while ii < len(lines) and lines[ii][j] == ".":
                lines[ii][j] = "O"
                lines[ii-1][j] = "."
                ii += 1
    for i in range(len(lines)):
        for j in range(len(lines[i])-1,-1,-1):
            if lines[i][j] != "O":
                continue
            jj = j + 1
            while jj < len(lines) and lines[i][jj] == ".":
                lines[i][jj] = "O"
                lines[i][jj-1] = "."
                jj += 1
def step():
    ans = 0
    dir()
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == "O":
                ans += len(lines) - i
    return ans

cycle = []
cache = {}
def h(grid):
    return "".join("".join(line) for line in grid)
for i in range(1000):
    res = step()
    ha = h(lines)
    if ha in cache:
        start = cache[ha]
        print(cycle[start + ((1000000000-start) % (len(cycle)-start+1))])
        break
    cycle.append(res)
    cache[ha] = i
