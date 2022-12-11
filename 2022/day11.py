from collections import deque
with open(0) as f:
    content = f.read()
    lines = content.splitlines()
    lines.append("")


class Monkey:
    def __init__(self):
        self.items = []
        self.to = []
        self.op = None
        self.test = 1

monkeys = []
mod = 1

monkey = Monkey()
for line in lines:
    if "Starting" in line:
        monkey.items = deque(map(int,line.split(": ")[-1].split(", ")))
    elif "Operation" in line:
        monkey.op = (line.split("= ")[-1])
    elif "Test" in line:
        monkey.test = int(line.split()[-1])
        mod *= monkey.test
    elif "true" in line or "false" in line:
        monkey.to.append(int(line.split()[-1]))
    elif "" == line:
        monkeys.append(monkey)
        monkey = Monkey()


inspected = [0] * len(monkeys)

# For part 1 replace 10000 by 20
for _ in range(10000):
    for i, monkey in enumerate(monkeys):
        while monkey.items:
            inspected[i] += 1
            item = monkey.items.popleft()
            current = eval(monkey.op.replace("old", str(item)))
            # For part 1
            # current //= 3
            current %= mod
            idx = monkey.to[current % monkey.test != 0]
            monkeys[idx].items.append(current)

l = sorted(inspected)
print(l[-2]*l[-1])