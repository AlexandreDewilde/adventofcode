content = open("input.txt").read()

lines = content.splitlines()
ans = 0

for line in lines:
    ints = list(map(int, line.split()))
    lst = ints[:]
    lsts = [ints]
    while True:
        diffs = []
        for i in range(len(lst)-1):
            diffs.append((lst[i+1] - lst[i]))
        lst = diffs[:]
        lsts.append(lst)
        if sum(diffs) == 0:
            break
    print(lsts)
    val = 0
    for i in range(len(lsts)-1, -1, -1):
        val = lsts[i][0] - val
        print(val, lsts[i][0])
    ans += val
print(ans)