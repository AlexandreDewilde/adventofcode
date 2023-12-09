content = open("input.txt").read()

lines = content.splitlines()
ans = 0

time = int("".join(lines[0].split(":")[1].split()))
distance = int("".join(lines[1].split(":")[1].split()))

totals = []
# time, record = times[i], distances[i]
l = 0
r = int(time) // 2
current = 0
while r > l:
    mid = (l + r) // 2
    t = (time - mid) * mid
    # print(mid, t, time, distance)
    if t > distance:
        r = mid
    else:
        l = mid + 1
first = r

rho = (time**2-4*distance)**0.5
l = (- time + rho) / -2
r = (- time - rho) / -2
import math

if l > r:
    l, r = r, l

ans = math.floor(r) - math.ceil(l) + 1
print(ans)