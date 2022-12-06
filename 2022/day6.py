from collections import deque
with open(f"input_6_2022.txt") as f:
    content = f.read()

#for task 1
#packet = deque(content[:3])
packet = deque(content[:13])
packet.appendleft(0)

for i in range(3, len(content)):
    packet.popleft()
    packet.append(content[i])
    #for task 1
    #if len(set(packet)) == 4:
    if len(set(packet)) == 14:
        print(i+1)
        break