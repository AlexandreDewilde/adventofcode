with open("input.txt") as f:
    content = f.read()

ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]

buttons = {}
inputs = {}
types = {}

for line in lines:
    s, e = line.split(" -> ")
    e = e.split(", ")
    type_ = "broadcaster"
    if s != "broadcaster":
        type_ = s[0]
        s = s[1:]
    buttons[s] = (type_, e)
    types[s] = type_
    for nxt in e:
        inputs[nxt] = inputs.get(nxt, []) + [s]


i = 0
from collections import defaultdict
poss = defaultdict(list)
def handle(current, prev, state, signal, q):
    if current not in buttons:
        return
    type_, nxt = buttons[current]
    if type_ == "broadcaster":
        for n in nxt:
            q.append((signal, n, current))
        state[current] = signal
    if type_ == "%" and signal == 0:
        if not state[current]:
            poss[current].append(i)
        state[current] ^= 1
        for n in nxt:
            q.append((state[current], n, current))
    if type_ == "&":
        pos = inputs[current].index(prev)
        if signal:
            state[current] |= 1 << pos
        else:
            state[current] &= ~ (1 << pos)
        snd = 0 if state[current] == (1<<len(inputs[current])) - 1 else 1
        for n in nxt:
            q.append((snd, n, current))
        if snd:
            poss[current].append(i)


state = {}
for btn, (type_, nxt) in buttons.items():
    state[btn] = 0


from collections import deque

while True:
    if i % 100000 == 0 and i:
        # print(poss)
        for btn in buttons:
            if btn not in poss:
                print(btn)
        break
    q = deque()
    handle("broadcaster", -1, state, 0, q)
    while q:
        signal, current, prev = q.popleft()
        handle(current, prev, state, signal, q)
    i += 1

ret = 1
for input in inputs["bb"]:
    ret *= (poss[input][0]+1)
print(ret)
