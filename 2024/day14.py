from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 14)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3"""
WIDTH = 101
HEIGHT = 103

pos = {}
vel = {}
for i, line in enumerate(puzzle_input.splitlines()):
    po, ve = line.split(" ")
    x, y = map(int, po[2:].split(","))
    vx, vy = map(int, ve[2:].split(","))
    if (x, y) not in pos:
        pos[(x, y)] = []
    pos[(x, y)].append(i)
    vel[i] = (vx, vy)

def iteration():
    global pos
    new_pos = {}
    for (x, y), el in (pos.items()):
        for i in el:
            xx = x+  vel[i][0]
            yy = y + vel[i][1]
            xx %= WIDTH
            yy %= HEIGHT
            if (xx, yy) not in new_pos:
                new_pos[(xx, yy)] = []
            new_pos[(xx, yy)].append(i)
    pos = new_pos

def print_grid():
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if (i, j) in pos:
                print(str(len(pos[(i, j)])), end="")
            else:
                print(".", end="")
        print()

for i in range(1000000):
    iteration()
    if all(len(el) == 1 for el in pos.values()):
        ans = i + 1
        break

# q1 = 0
# for i in range(WIDTH // 2):
#     for j in range(HEIGHT // 2):
#         q1 += len(pos.get((i, j), []))

# q2 = 0
# for i in range(WIDTH // 2 + 1, WIDTH):
#     for j in range(HEIGHT // 2):
#         q2 += len(pos.get((i, j), []))

# q3 = 0
# for i in range(WIDTH // 2):
#     for j in range(HEIGHT // 2 + 1, HEIGHT):
#         q3 += len(pos.get((i, j), []))

# q4 = 0
# for i in range(WIDTH // 2 + 1, WIDTH):
#     for j in range(HEIGHT // 2 + 1, HEIGHT):
#         q4 += len(pos.get((i, j), []))

# ans = q1 * q2 * q3 * q4
print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)