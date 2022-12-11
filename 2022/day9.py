with open(f"input_9_2022.txt") as f:
    content = f.read()
    lines = content.splitlines()

# For part 1 replace 10 by 2
queue = [(0,0)]*10
vis = set()

def is_in(x,y):
    for i in range(-1,2):
        for j in range(-1,2):
            if (queue[x][0] + i, queue[x][1] + j) == queue[y]:
                return True
    return False

def update():
    for i in range(1,len(queue)):
        if not is_in(i-1, i):
            x,y = queue[i]
            x += (x != queue[i-1][0]) * (-1 if queue[i-1][0] - x < 0 else 1)
            y += (y != queue[i-1][1]) * (-1 if queue[i-1][1] - y < 0 else 1)
            queue[i] = (x,y)
    vis.add(queue[-1])

for line in lines:
    direction, dst = line.split()
    for i in range(int(dst)):
        if direction == "U":
            queue[0] = (queue[0][0], queue[0][1] + 1)            
        elif direction == "D":
            queue[0] = (queue[0][0], queue[0][1] - 1)
        elif direction == "L":
            queue[0] = (queue[0][0] - 1, queue[0][1])
        else:
            queue[0] = (queue[0][0] + 1, queue[0][1])
        update()
    
print(len(vis))

