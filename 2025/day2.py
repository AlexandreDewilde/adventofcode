ranges = open("input").read().strip().split(",")

ans = 0
for i in range(len(ranges)):
    start, end = list(map(int, ranges[i].split("-")))

    for el in range(start, end + 1):
        s = str(el)
        mid = len(s) // 2
        for seq_len in range(1, mid + 1):
            if s.count(s[:seq_len]) * seq_len == len(s):
                ans += el
                break

print(ans)
