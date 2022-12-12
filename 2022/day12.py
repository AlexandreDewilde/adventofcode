from collections import deque

with open(0) as f:
    content = f.read()
    lines = content.splitlines()

s = []
e = (0,0)

for i in range(len(lines)):
    lines[i] = list(lines[i])
    for j in range(len(lines[i])):
        if lines[i][j] in {"S", "a"}:
            s.append((i, j))
            lines[i][j] = "a"
        elif lines[i][j] == "E":
            e = (i,j)
            lines[i][j] = "z"

q = deque(s)
dst = [[float("inf") for _ in range(len(lines[i]))] for i in range(len(lines))]

for i, j in s:
    dst[i][j] = 0
    
delta = [(0,1), (0,-1), (-1,0), (1,0)]
while q:
    x, y = q.popleft()
    for r in range(4):
        xx = x + delta[r][0]
        yy = y + delta[r][1]
        if 0 <= xx < len(lines) and 0 <= yy < len(lines[xx]) and ord(lines[xx][yy])-ord(lines[x][y]) <= 1 and dst[xx][yy] == float("inf"):
            dst[xx][yy] = dst[x][y] + 1
            q.append((xx, yy))

print(dst[e[0]][e[1]])


