with open("input.txt") as f:
    content = f.read()

lines = content.splitlines()
# print(lines)
ans = 0

import heapq
def di(i, j):
    dst = [[float("inf") for _ in range(len(lines[0]))] for _ in range(len(lines))]
    pq = [(0, i, j)]
    dst[i][j] = 0
    while pq:
        d, i, j = heapq.heappop(pq)
        if d > dst[i][j]:
            continue
        for di, dj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
            if 0 <= di < len(lines) and 0 <= dj < len(lines[0]):
                
                dd = 1000000 if all("#" != char for char in lines[di]) or all("#" != lines[ddj][dj] for ddj in range(len(lines))) else 1
                if dst[di][dj] > dst[i][j] + dd:
                    dst[di][dj] = dst[i][j] + dd
                    heapq.heappush(pq, (dst[di][dj], di, dj))
    return dst

g = []
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == "#":
            g.append((i,j))

ans = 0

for idx in range(len(g)):
    if idx % 10 == 0:
        print(idx)
    i,j = g[idx]
    dst = di(i,j)
    # print(dst)
    # print(idx)
    for idx2 in range(idx+1, len(g)):
        # print(idx2)
        x, y = g[idx2]
        ans += dst[x][y]
        # print(dst[x][y], idx, idx2, g[idx], g[idx2])
print(ans)