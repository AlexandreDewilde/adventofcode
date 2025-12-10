from z3 import *

lines = open("input").read().strip().split("\n")

ans = 0

for line in lines:
    ons, *buttons, joltages = line.split()
    res_mask = [0 if el == "." else 1 for el in ons[1:-1]]
    buttons_mask = []
    for button in buttons:
        parse_button = list(map(int, button[1:-1].split(",")))
        buttons_mask.append(
            [0 if i not in parse_button else 1 for i in range(len(res_mask))]
        )

    joltage_mask = tuple([int(x) for x in joltages[1:-1].split(",")])

    res_mask = int("".join(map(str, res_mask)), 2)
    buttons_mask = [int("".join(map(str, bm)), 2) for bm in buttons_mask]

    # def dp(i, current):
    #     if current == res_mask:
    #         return 0
    #     if i == len(buttons_mask):
    #         return float("inf")
    #     return min(dp(i + 1, current), dp(i + 1, current ^ buttons_mask[i]) + 1)

    # from functools import cache

    buttons_mask = sorted(buttons_mask, key=lambda x: bin(x).count("1"))

    # too slow
    # @cache
    # def dp(current, i):
    #     if all(c == 0 for c in current):
    #         return 0
    #     if i == len(buttons_mask):
    #         return None

    #     mn = min(
    #         current[j]
    #         for j in range(len(joltage_mask))
    #         if (1 << len(joltage_mask) - 1 - j) & buttons_mask[i]
    #     )

    #     for j in range(mn + 1):
    #         new_current = tuple(
    #             current[k]
    #             - (1 if (1 << len(joltage_mask) - 1 - k) & buttons_mask[i] else 0) * j
    #             for k in range(len(joltage_mask))
    #         )

    #         res = dp(new_current, i + 1)
    #         if res is not None:
    #             return res + j

    # res = dp(joltage_mask, 0)
    # ans += res

    presses = [Int(f"press_{i}") for i in range(len(buttons_mask))]

    o = Optimize()
    o.add([p >= 0 for p in presses])
    for j in range(len(joltage_mask)):
        o.add(
            Sum(
                [
                    presses[i]
                    * (1 if (1 << len(joltage_mask) - 1 - j) & buttons_mask[i] else 0)
                    for i in range(len(buttons_mask))
                ]
            )
            == joltage_mask[j]
        )
    o.minimize(Sum(presses))
    print(o.check(), o.model(), o.model().evaluate(Sum(presses)))
    ans += o.model().evaluate(Sum(presses)).as_long()
print(Sum(ans))
