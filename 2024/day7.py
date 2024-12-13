from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 7)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """190: 10 19
# 3267: 81 40 27
# 83: 17 5
# 156: 15 6
# 7290: 6 8 6 15
# 161011: 16 10 13
# 192: 17 8 14
# 21037: 9 7 18 13
# 292: 11 6 16 20"""

def poss(res, nb, i, current):
    if i >= len(nb):
        return res == current
    if i == 0:
        return poss(res, nb, i + 1, nb[i])
    return any([poss(res, nb, i + 1, current + nb[i]), poss(res, nb, i + 1, current * nb[i]), poss(res, nb, i + 1, int(str(current) +  str(nb[i])))])

for line in puzzle_input.splitlines():
    res, nb = line.split(":")
    res = int(res)
    nb = list(map(int, nb.split()))
    if poss(res, nb, 0, 0):
        ans += res
print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)