with open("input.txt") as f:
    content = f.read()
ans = 0
lines = content.splitlines()


def apply(s):
    ret = 0
    for c in s:
        ret += ord(c)
        ret *= 17
        ret %= 256
        
    return ret

lst = [{} for _ in range(256)]
for s in lines[0].split(","):
    if "=" in s:
        idx = s.index("=")
        box = apply(s[:idx])
        nb = int(s[idx+1:])
        lst[box][s[:idx]] = nb
        continue
    idx = s.index("-")
    box = apply(s[:idx])
    label = s[:idx]
    if label in lst[box]:
        del lst[box][label]
    
for i in range(len(lst)):
    for j, v in enumerate(lst[i].values()):
        ans += (i + 1) * (j+1) * v

print(ans)