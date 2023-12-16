with open("input.txt") as f:
    content = f.read()

ans = 0
lines = content.splitlines()
import sys
sys.setrecursionlimit(int(1e5))
vis = set()
def dfs(current, i, j):
    if (current, i, j) in vis:
        return
    vis.add((current, i, j))
    # print(current, i, j)
    if current == ">" and j + 1 < len(lines[i]):
        if lines[i][j+1] in {".", "-"}:
            dfs(current, i, j+1)
        if lines[i][j+1] == "|":
            dfs("v", i, j+1)
            dfs("^", i, j+1)
        if lines[i][j+1] == "\\":
            dfs("v", i, j+1)
        if lines[i][j+1] == "/":
            dfs("^", i, j+1)
    if current == "v" and i + 1 < len(lines):
        char = lines[i+1][j]
        if char in {"|", "."}:
            dfs(current, i+1, j)
        elif char == "-":
            dfs("<", i+1, j)
            dfs(">", i+1, j)
        elif char == "/":
            dfs("<", i+1, j)
        else:
            dfs(">", i+1, j)
    if current == "<" and j > 0:
        char = lines[i][j-1]
        if char in {".", "-"}:
            dfs(current, i, j-1)
        if char == "|":
            dfs("v", i, j-1)
            dfs("^", i, j-1)
        if char == "\\":
            dfs("^", i, j-1)
        if char == "/":
            dfs("v", i, j-1)
    if current == "^" and i > 0:
        char = lines[i-1][j]
        if char in {"|", "."}:
            dfs(current, i-1, j)
        elif char == "-":
            dfs("<", i-1, j)
            dfs(">", i-1, j)
        elif char == "\\":
            dfs("<", i-1, j)
        else:
            dfs(">", i-1, j)       
for i in range(len(lines)):
    vis.clear()
    dfs(">", i, -1)
    ans = max(ans, len(set([(i,j) for _, i, j in vis if j >= 0])))
for i in range(len(lines)):
    vis.clear()
    dfs("<", i, len(lines))
    ans = max(ans, len(set([(i,j) for _, i, j in vis if j < len(lines)])))
for j in range(len(lines[0])):
    vis.clear()
    dfs("v", -1, j)
    ans = max(ans, len(set([(i,j) for _, i, j in vis if i >= 0])))
for j in range(len(lines[0])):
    vis.clear()
    dfs("^", len(lines[0]), j)
    ans = max(ans, len(set([(i,j) for _, i, j in vis if i < len(lines)])))