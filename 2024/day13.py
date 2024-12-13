from aoctools import *
from functools import cmp_to_key
from math import gcd

aocd = AOCD(2024, 13)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400

# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176

# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450

# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279"""

devices = puzzle_input.split("\n\n")



def solve(device):
    a, b, prize = device.splitlines()
    a = a.split(": ")[1]
    b = b.split(": ")[1]
    prize = prize.split(": ")[1]
    ax = a.split(", ")
    bx = b.split(", ")
    prize = prize.split(", ")
    a1 = int(ax[0][2:])
    a2 = int(ax[1][2:])
    b1 = (int(bx[0][2:]))
    b2 = (int(bx[1][2:]))
    prize_x = (int(prize[0][2:])) + 10000000000000
    prize_y = (int(prize[1][2:])) + 10000000000000

    y = (prize_y - a2 / a1 * prize_x) / (b2 - a2 / a1 * b1)
    x = (prize_x - b1 * y) / a1
    x = round(x)
    y = round(y)
    if abs(a1 * x + b1 * y - prize_x) > 1e-6 or abs(a2 * x + b2 * y - prize_y) > 1e-6:
        return 0
    return x * 3 + y
for device in devices:
    ans += solve(device)
print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)