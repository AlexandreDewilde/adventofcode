content = open("input.txt").read()

ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]

workflows, starts = content.split("\n\n")


conds = {}
for w in workflows.splitlines():
    name, cond = w.split("{")
    cond = cond[:-1]
    cond = cond.split(",")
    conds[name] = cond
import copy

def combs(vals):
    ret = 1
    for rang in vals.values():
        if rang[1] < rang[0]:
            return 0
        ret *= rang[1] - rang[0] + 1
    return ret
def go(vals, current):
    if current == "A":
        print(vals)
        return combs(vals)
    if current == "R":
        return 0
    vals = copy.deepcopy(vals)
    ret = 0
    for cond in conds[current]:
        if ":" not in cond:
            ret += go(vals, cond)
            continue

        cnd, goto = cond.split(":")
        value = int(cnd[2:])
        prev = vals[cnd[0]][:]
        if cnd[1] == ">":
            vals[cnd[0]][0] = max(value+1, prev[0])
            ret += go(vals, goto)
            vals[cnd[0]][0] = prev[0]
            vals[cnd[0]][1] = min(vals[cnd[0]][1], value)
        else:
            vals[cnd[0]][1] = min(value-1, prev[1])
            ret += go(vals, goto)
            vals[cnd[0]][1] = prev[1]
            vals[cnd[0]][0] = max(vals[cnd[0]][0], value)
    return ret

vals = {letter: [1,4000] for letter in "xmas"}
ans = go(vals, "in")
