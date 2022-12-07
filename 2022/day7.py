with open(f"input_7_2022.txt") as f:
    content = f.read()
    lines = content.splitlines()

class Node:
    def __init__(self, prev=None):
        self.prev = prev
        self.next = {}
        self.size = 0


current = Node()
first = current
for line in lines[0:]:
    infos = line.split()
    if "$ cd .." == line:
        current = current.prev
    elif infos[1] == "cd":
        directory = line.split()[-1]
        if directory not in current.next:
            current.next[directory] = Node(current)
        current = current.next[directory]
    elif infos[0] != '$' and len(infos) == 2 and infos[0] != 'dir':
        current.size += int(infos[0])

ans = [0]
def calcul(current):
    total = current.size
    for adj in current.next.values():
        total += calcul(adj)
    if total < 100000:
        ans[0] += total
    current.size = total
    return total

calcul(first)

print(ans[0])

def rec(current):
    mi = float("inf")
    if 70000000 - first.size + current.size >= 30000000:
        mi = current.size
    for adj in current.next.values():
        mi = min(rec(adj), mi)
    return mi
print(rec(first))