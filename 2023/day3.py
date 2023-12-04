import requests
import os

content = ""
if not os.path.exists("input.txt"):
    cookies = {"session": os.environ["SESSION_AOC"]}
    content = requests.get("https://adventofcode.com/2023/day/3/input",
        cookies=cookies,
        headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0"}
    ).text
    with open("input.txt", "w") as f:
        f.write(content)
else:
    with open("input.txt") as f:
        content = f.read()


# content = ""
# for _ in range(10):
#     content += input() + "\n"
# content = content[:-1]

lines = content.splitlines()


# ints = list(map(int, lines))
# floats = list(map(float, lines))
grid = [list(line) for line in content.splitlines()]
# has_ajd = lambda i, j: any(grid[i+di][j+dj] != "." and not grid[i+di][j+dj].isnumeric() for di in range(-1,2) for dj in range(-1,2) if i != j != 0)
numbers = []
from collections import deque

def has_adj(i,j):
    gears = []
    for x in range(-1,2):
        for y in range(-1, 2):
            if x == y == 0:
                continue
            ii = i + x
            jj = j + y
            if 0<= ii < len(grid) and 0 <= jj < len(grid) and grid[ii][jj] == "*":
                gears.append((ii, jj))
    return gears
current = 0
current_gears = set()

coords = {}
# numbers = []
for i in range(len(lines)):
    for j in range(len(lines[i])):
        if grid[i][j].isnumeric():
            current = 10 * current + int(grid[i][j])
            for el in has_adj(i,j):
                current_gears.add(el)        
            
        elif not grid[i][j].isnumeric():
            if current_gears:
                print(current_gears, current)
            for coord in current_gears:
                if coord not in coords:
                    coords[coord] = []
                coords[coord].append(current)
            current = 0
            current_gears = set()
    for coord in current_gears:
        if coord not in coords:
            coords[coord] = []
        coords[coord].append(current)
    current = 0
    current_gears = set()
# print(grid[:2])
# vis = [[False]*len(lines[0]) for i in range(len(lines))]
print(coords)
total = 0
for i, j in coords:
    current = 1
    if len(coords[(i,j)]) != 2:
        continue
    for nb in coords[(i,j)]:
        current *= nb
    total += current
print(total)