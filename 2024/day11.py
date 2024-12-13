from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 11)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732"""

stones = {}

for nb in map(int, puzzle_input.split(" ")):
    stones[nb] = stones.get(nb, 0) + 1

for i in range(75):
    new_stones = {}
    for k,v in stones.items():
        if k == 0:
            new_stones[1] = new_stones.get(1, 0) + v
        elif len(str(k)) % 2 == 0:
            first_half = int(str(k)[:len(str(k)) // 2])
            second_half = int(str(k)[len(str(k)) // 2:])
            new_stones[first_half] = new_stones.get(first_half, 0) + v
            new_stones[second_half] = new_stones.get(second_half, 0) + v
        else:
            new_stones[2024 * k] = new_stones.get(2024 * k, 0) + v
    stones = new_stones

ans = sum(stones.values())
print(ans)
input()
aocd.p1(ans)
input()
aocd.p2(ans)