with open("input.txt") as f:
    content = f.read()

lines = content.splitlines()
ans = 0

for line in lines:
    row, nbs = line.split()
    nbs = list(map(int, nbs.split(",")))
    print(row)
    row = "?".join([row for _ in range(5)])
    nbs = nbs*5
    mapping = {}
    def dp(i, j, current):
        if (i,j,current) in mapping:
            return mapping[(i,j,current)]

        condj = (j == len(nbs)-1 and current==nbs[-1])
        if (j == len(nbs) or condj) and i == len(row):
            return 1
        if i >= len(row):
            return 0
        if j >= len(nbs):
            return 0 if row[i] == "#" or current else dp(i+1, j, 0)
        tot = 0
        if current > nbs[j]:
            return 0
        if current == nbs[j] and row[i] != "#":
            tot += dp(i+1, j+1, 0)

        if row[i] == "#":
            tot += dp(i+1, j, current+1)
        elif row[i] == "?":
            if not current:
                tot += dp(i+1, j, 0)
            tot += dp(i+1, j, current + 1)
        else:
            if not current:
                tot += dp(i+1, j, 0)
        mapping[(i,j,current)] = tot
        return tot
    ans += dp(0, 0, 0)

    

print(ans)
