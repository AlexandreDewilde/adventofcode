with open("input.txt") as f:
    content = f.read()
lines = content.splitlines()
ans = 0

grid = [list(line) for line in lines]

start = None
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if grid[i][j] == "S":
            start = (i, j)
            break

from collections import deque


augmented_grid = [[False for _ in range(len(lines[0])*3)] for _ in range(len(lines)*3)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i][j] == "|":
            augmented_grid[i*3][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+2][j*3+1] = True
        if grid[i][j] == "-":
            augmented_grid[i*3+1][j*3] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3+2] = True
        if grid[i][j] == "L":
            augmented_grid[i*3][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3+2] = True 
        if grid[i][j] == "J":
            augmented_grid[i*3][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3] = True
        if grid[i][j] == "7":
            augmented_grid[i*3+2][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3] = True
        if grid[i][j] == "F":
            augmented_grid[i*3+2][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3+2] = True

dst = [[float("inf") for _ in range(len(lines[0])*3)] for _ in range(len(lines)*3)]
# q = deque([])
# for i in range(3):
#     for j in range(3):
#         if i == j == 1:
#             continue
#         q.append((start[0]*3+i, start[1]*3+j))

# for i, j in q:
#     dst[i][j] = 0

# while q:
#     i, j = q.popleft()
#     for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
#         if 0 <= ii < len(augmented_grid) and 0<= jj < len(augmented_grid[0]) and dst[ii][jj] == float("inf") and augmented_grid[ii][jj]:
#             dst[ii][jj] = dst[i][j] + 1
#             q.append((ii, jj))

# for i in range(len(augmented_grid)):
#     ans = max(ans, max(el if el != float("inf") else -1 for el in dst[i]))
# ans = ans // 3 + 1

import sys
sys.setrecursionlimit(int(1e5))

def dfs(i, j, vis, par):
    vis[i][j] = True
    f = set([(i//3,j//3)])
    end = False
    for ii, jj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if 0 <= ii < len(augmented_grid) and 0<= jj < len(augmented_grid[0]) and augmented_grid[ii][jj] and par != (ii,jj):
            if vis[ii][jj]:
                return True, f
            res, path = dfs(ii, jj, vis, (i,j))
            end |= res
            if res:
                f |= path
    return end, f
def get_inside(path):
    inside = [[False]*len(grid[0]) for _ in range(len(grid))]

    for i in range(len(grid)):
        current = False
        s = ""
        for j in range(len(grid[i])):
            if (i,j) in path and grid[i][j] == "|":
                current ^= 1
            if (i,j) in path and grid[i][j] not in {".", "-", "|"}:
                s += grid[i][j]
            if s == "L7" or s == "FJ":
                current ^= 1
            
            if len(s) >= 2:
                s = ""
            inside[i][j] = current
    return inside
for char in "|-LJ7F":
    i, j = start
    di = dj = 0
    copy = [line[:] for line in augmented_grid]
    if char== "|":
        dj = 1
        augmented_grid[i*3][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+2][j*3+1] = True
    if char == "-":
        di = 1
        augmented_grid[i*3+1][j*3] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3+2] = True
    if char == "L":
        dj = 1
        augmented_grid[i*3][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3+2] = True 
    if char == "J":
        dj = 1
        augmented_grid[i*3][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3] = True
    if char == "7":
        di = 2
        dj = 1
        augmented_grid[i*3+2][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3] = True
    if char == "F":
        di = 2
        dj = 1
        augmented_grid[i*3+2][j*3+1] = augmented_grid[i*3+1][j*3+1] = augmented_grid[i*3+1][j*3+2] = True
    grid[i][j] = char    
    vis = [[False for _ in range(len(lines[0])*3)] for _ in range(len(lines)*3)]
    res, path = dfs(start[0]*3+di, start[1]*3+dj, vis, (-1,-1))
    if res:
        inside = get_inside(path)
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if inside[i][j] and (i,j) not in path:
                    ans += 1
        print(ans)
        # print(inside)
        # for i in range(len(grid)):
        #     for j in range(len(grid[0])):
        #         if (i, j) in path:
        #             print(grid[i][j], end="")
        #         else:
        #             print("I" if inside[i][j] else "O", end="")
        #     print()
    augmented_grid = copy
# for i in range(3):
#     for j in range(3):
#         if i == j == 1:
#             continue
#         vis = [[False for _ in range(len(lines[0])*3)] for _ in range(len(lines)*3)]
#         for ii in range(3):
#             for jj in range(3):
#                 vis[start[0]+ii][start[1]+jj] = True
#         res, path = dfs(start[0]*3+i, start[1]*3+j, vis, (-1,-1))
#         if res:
#             print(res)
#             ans = 0
#             for i in range(len(grid)):
#                 for j in range(len(grid)):
#                     if grid[i][j] == "." and cnt(i, j, path) % 2:
#                         ans += 1
#                     # print(i,j)
#             submit(day, 2, ans)
# submit(day, 1, ans)