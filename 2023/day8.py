content = open("input.txt").read()

lines = content.splitlines()
ans = 0

seq = lines[0]

class Node:
    def __init__(self, name):
        self.name = name
        self.l = None
        self.r = None

match = {}
currents = []
for line in lines[2:]:
    x, _ = line.split(" = ")
    match[x] = Node(x)
    if x[-1] == "A":
        currents.append(match[x])

for line in lines[2:]:
    x, y = line.split(" = ")
    l, r = y.split(", ")
    l = l[1:]
    r = r[:-1]
    match[x].l = match[l]
    match[x].r = match[r]


ends = []
for current in currents:
    end = 0
    for i in range(1000000):
        if current.name[-1] == "Z":
            end = i
            break
        char = seq[i%len(seq)]
        if char == "L":
            current = current.l
        else:
            current = current.r
    ends.append(end)

from math import lcm
current = ends[0]
for end in ends:
    current = lcm(current, end)

ans = current
print(ans)