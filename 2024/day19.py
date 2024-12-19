from aoctools import *
from functools import cmp_to_key
import random
from collections import deque
import heapq

aocd = AOCD(2024, 19)
puzzle_input = aocd.as_str
ans = 0


# puzzle_input = """r, wr, b, g, bwu, rb, gb, br

# brwrr
# bggr
# gbbr
# rrbgbr
# ubwu
# bwurrg
# brgr
# bbrgwb"""


poss = set(puzzle_input.splitlines()[0].split(", "))
patterns = puzzle_input.splitlines()[2:]

import sys
sys.setrecursionlimit(10**6)

mem = {}
def dfs(pattern, to_process):
    if (pattern, to_process) in mem:
        return mem[(pattern, to_process)]
    if pattern == "":
        # if to_process in poss:
        #     print(ans, to_process)
        return 1 if to_process == "" or to_process in poss else 0

    ret = 0
    if to_process in poss:
        ret += dfs(pattern[1:], pattern[0])

    ret += dfs(pattern[1:], to_process + pattern[0])
    mem[(pattern, to_process)] = ret
    return mem[(pattern, to_process)]

for i, line in enumerate(puzzle_input.splitlines()[2:]):
    ans += dfs(line.strip(), "")
    # print(dfs(line.strip(), ""))
    # print(i, ans)

print(ans)
input()
aocd.p1(ans)
input()
aocd.p2(ans)