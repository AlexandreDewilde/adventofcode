from aoctools import *

aocd = AOCD(2024, 2)
puzzle_input = aocd.as_str
ans2 = 0
ans = 0
# nb = aocd.as_int
# s = aocd.as_str
# nbs = aocd.ilist
# strings = aocd.slist

# puzzle_input = """7 6 4 2 1
# 1 2 7 8 9
# 9 7 6 2 1
# 1 3 2 4 5
# 8 6 4 4 1
# 1 3 6 7 9"""

for line in puzzle_input.splitlines():
    lsT = list(map(int, line.split(" ")))
    poss = False
    for i in range(len(lsT)):
    # print(lst)
        lst = lsT.copy()
        lst.pop(i)
        for i in range(len(lst) - 1):
            if 1 <= lst[i + 1] - lst[i] <= 3:
                pass
            else:
                break
        else:
            poss += 1
        for i in range(len(lst) - 1):
            if 1 <= lst[i] - lst[i + 1] <= 3:
                pass
            else:
                break
        else:
            poss += 1
    if poss:
        ans2 += 1
# print(ans)
# calculate the answers
# aocd.p1(ans)
aocd.p2(ans2)