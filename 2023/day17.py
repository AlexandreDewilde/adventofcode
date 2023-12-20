content = open("input.txt").read()

ans = 0
lines = content.splitlines()

import heapq

pq = [(0,"",0,0,0)]

dst = {}

dst[(0,0,"",0)] = 0

while pq:
    d, current, cons, i, j = heapq.heappop(pq)
    if d > dst[(i,j,current,cons)]:
        continue

    for ii, jj, sign in [(i+1, j, "v"), (i-1, j, "^"), (i, j-1, "<"), (i, j+1, ">")]:
        new_cons = cons + 1 if sign == current else 1
        if current != "" and ((sign != current and cons < 4) or (sign == current and cons >= 10)):
            continue
        if  ((sign == ">" and current == "<")
                or (sign == "^" and current == "v")
                or (sign == "v" and current == "^")):
                continue
        if 0 <= ii < len(lines) and 0 <= jj < len(lines[0]) and dst.get((ii,jj,sign,new_cons), float("inf")) > d + int(lines[ii][jj]):
            dst[(ii,jj,sign, new_cons)] = d + int(lines[ii][jj])
            heapq.heappush(pq, (dst[(ii,jj,sign, new_cons)], sign, new_cons, ii, jj))

ans = float("inf")
# print(dst)
for (i, j, sign, cons), val in dst.items():
    if i == len(lines) - 1 and j == len(lines[0]) -1 and cons >= 4:
        ans = min(ans, val)
print(ans)