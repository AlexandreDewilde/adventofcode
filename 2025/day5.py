ranges, ingredients = open("input").read().strip().split("\n\n")


ranges = [list(map(int, r.split("-"))) for r in ranges.split("\n")]
ingredients = [int(i) for i in ingredients.split("\n")]

ranges.sort()
ingredients.sort()


current_range_idx = 0
ans = 0
# for ingredient in ingredients:
#     while (
#         ingredient > ranges[current_range_idx][1]
#         and current_range_idx < len(ranges) - 1
#     ):
#         current_range_idx += 1

#     if ranges[current_range_idx][0] <= ingredient <= ranges[current_range_idx][1]:
#         ans += 1

mx = ranges[0][1]
for i in range(len(ranges)):
    start, end = ranges[i]
    start = max(start, mx + 1) if i > 0 else start
    mx = max(mx, end)
    if end >= start:
        ans += end - start + 1
    # print(start, end, ans)
print(ans)
