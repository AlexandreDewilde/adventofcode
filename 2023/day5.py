content = open("input.txt").read()

lines = content.splitlines()
ans = 0

seeds = list(map(int, lines[0].split(": ")[1].split()))

pairs = []
for i in range(0,len(seeds), 2):
    pairs.append((seeds[i], seeds[i] - 1 + seeds[i+1]))
pairs.sort()
transitions = []
for block in content.split("\n\n")[1:]:
    block = block.split("\n")
    transition = block[0].split()[0]
    start, end = transition.split("-to-")
    transitions.append([])
    for line in block[1:]:
        if not line: continue
        d, s, l = map(int, line.split())
        transitions[-1].append((d,s,s+l-1))

ans = float("inf")
from collections import deque
current_lst = deque(pairs)

for both in transitions:
    new_current_lst = []
    while current_lst:
        start, end = current_lst.popleft()
        for transition in both:
            if transition[1] <= start <= end <= transition[2]:
                current = transition[0] + start - transition[1]
                current_end = current + (end - start)
                new_current_lst.append((current, current_end))
                break
            elif transition[1] <= start <= transition[2]:
                current = transition[0] + start - transition[1]
                current_end = transition[0] + (transition[2] - transition[1])
                new_current_lst.append((current, current_end))
                current_lst.append((transition[2]+1, end))
                break
            elif transition[1] <= end <= transition[2]:
                current_end = transition[0] + (end - transition[1])
                new_current_lst.append((transition[0], current_end))
                current_lst.append((start, transition[1]-1))
                break
        
            elif start <= transition[1] <= transition[2] <= end:
                current_lst.append((start, transition[1]-1))
                current_lst.append((transition[2]+1, end))
                # new_current_lst.append((transition[0], transition[0] + (transition[2] - transition[0])))
                break
        else:
            new_current_lst.append((start, end))
    current_lst = new_current_lst
    current_lst.sort()
    current_lst = deque(current_lst)


ans = (min(list(current_lst), key=lambda x: x[0])[0])
print(ans)