from functools import cache

batteries = open("input").read().strip().split("\n")


@cache
def best(s, idx, selected=0):
    if selected == 12:
        return 0
    if selected + idx + 1 < 12:
        return float("-inf")
    take = int(s[idx]) + best(s, idx - 1, selected + 1) * 10
    not_take = best(s, idx - 1, selected)
    return max(take, not_take)


ans = 0
for el in batteries:
    ans += best(el, len(el) - 1)

print(ans)
