from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 5)
puzzle_input = aocd.as_str
ans = 0

order, updates = puzzle_input.split("\n\n")

order = order.splitlines()
updates = updates.splitlines()

order_dic = {}
inv_order_dic = {}
for line in order:
    line = list(map(int, line.split("|")))
    if line[0] not in order_dic:
        order_dic[line[0]] = []
    if line[1] not in inv_order_dic:
        inv_order_dic[line[1]] = []
    order_dic[line[0]].append(line[1])
    inv_order_dic[line[1]].append(line[0])

def correct(el):
    current = set()
    for e in el:
        if e in current:
            return False
        for nb in inv_order_dic[e]:
            if nb not in current:
                current.add(nb)
    return True

def reordered(lst):
    def cmp(x, y):
        if x in order_dic.get(y, []):
            return -1
        if y in order_dic.get(x, []):
            return 1
        return 0

    return sorted(lst, key=cmp_to_key(cmp))

for line in updates:
    lst = list(map(int, line.split(",")))
    # if correct(lst):
    #     ans += lst[len(lst) // 2]

    if not correct(lst):
        reorder = reordered(lst)
        ans += reorder[len(lst) // 2]
print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)