from functools import cmp_to_key

with open(0) as f:
    content = f.read()
    lines = content.splitlines()

def compare(l, l2):
    for i in range(min(len(l), len(l2))):
        res = 0
        if type(l[i]) == list and type(l2[i]) == list:
            res = compare(l[i], l2[i])
        elif type(l[i]) == list:
            res = compare(l[i], [l2[i]])
        elif type(l2[i]) == list:
            res = compare([l[i]], l2[i])
        else:
            res = int(l[i]) - int(l2[i])
        if res != 0:
            return res
    return len(l) - len(l2)

idx = 1
t = []
ans = 0
for i in range(0,len(lines), 3):
    l1 = eval(lines[i])
    l2 = eval(lines[i+1])

    if compare(l1, l2) < 0:
        ans += idx
    t.append(l1)
    t.append(l2)
    idx += 1

print(ans)

t.append([[2]])
t.append([[6]])
t.sort(key=cmp_to_key(compare))

print((t.index([[2]]) + 1) * (t.index([[6]])+1))

    