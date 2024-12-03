from aoctools import *
import re

aocd = AOCD(2024, 3)
puzzle_input = aocd.as_str
ans = 0

regex = re.compile(r"mul\((\d+),(\d+)\)")
regex = re.compile(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)")

do = True
for pattern in re.finditer(regex, puzzle_input):
    s = pattern.group()
    if s.startswith("mul") and do:
        ans += int(pattern[1]) * int(pattern[2])
    elif s == "do()":
        do = True
    elif s == "don't()":
        do = False

print(ans)
# calculate the answers
# aocd.p1(ans)
# aocd.p2(ans)