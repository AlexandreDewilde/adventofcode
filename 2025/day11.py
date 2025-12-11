lines = open("input").read().strip().split("\n")

g = {}

for line in lines:
    start, *ends = line.split()
    start = start[:-1]
    if start not in g:
        g[start] = []
    for end in ends:
        g[start].append(end)
from functools import cache


@cache
def dp(node, dac, fft):
    if node == "out":
        return dac and fft
    res = 0
    for nei in g.get(node, []):
        res += dp(nei, dac | (nei == "dac"), fft | (nei == "fft"))
    return res


# print(dp("you"))
print(dp("svr", False, False))
