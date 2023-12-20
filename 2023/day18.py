content = open("input.txt").read()

ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]

i = 0
j = 0

addi = 0
addj = 0
edges = []
total = 0
for line in lines:
    ii, jj = i, j
    d, s, c = line.split()
    s = int(s)
    d = "RDLU"[int(c[-2])]
    s = int(c[2:-2], 16)
    if d == "U":
        i -= s
    elif d == "R":
        j += s
    elif d == "D":
        i += s
    else:
        j -= s
    edges.append((i,j))
    total += abs(ii - i) + abs(jj - j)

for i in range(len(edges)):
    ans += (edges[i][0] + edges[(i+1)%len(edges)][0]) * (edges[(i+1)%len(edges)][1] - edges[i][1])


ans = abs(ans) // 2 + total // 2 + 1