from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 9)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """2333133121414131402"""

nb = list(map(int, puzzle_input))

space = []
space_id = []
current = 0
free_space = []
for i in range(len(nb)):
    if i % 2 == 0:
        for j in range(current, current+nb[i]):
            # space.append(j)
            space_id.append(i // 2)
        current += nb[i]
    else:
        for j in range(current, current+nb[i]):
            # space.append(j)
            space_id.append(".")
        free_space.append([current, nb[i]])
        current += nb[i]

# i = 0
j = len(space_id) - 1
while j >= 0:
    print(j)
    if space_id[j] == ".":
        j -= 1
        continue
    start_file = j
    while start_file > 0 and space_id[j] == space_id[start_file - 1]:
        start_file -= 1

    length = j - start_file + 1
    # print("length", length)
    new_start = None
    idx_av = None
    for i, (idx, av) in enumerate(free_space):
        if av >= length and idx < start_file:
            new_start = idx
            idx_av = i
            break
    if new_start is None:
        j = start_file - 1
        continue

    for i in range(length):
        space_id[new_start + i] = space_id[start_file + i]
        space_id[start_file + i] = "."
    # print("".join(map(str, space_id)))

    free_space[idx_av][1] -= length
    free_space[idx_av][0] += length
    j = start_file - 1
    # print(free_space)

print("".join(map(str, space_id)))
for i, el in enumerate(space_id):
    if el != ".":
        ans += i * el

print(ans)
input()
# aocd.p1(ans)
# input()
aocd.p2(ans)