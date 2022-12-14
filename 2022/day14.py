with open(0) as f:
    content = f.read()
    lines = content.splitlines()

grid = set()
mx = 0
for line in lines:
    coords = line.split(" -> ")
    a,b = map(int, coords[0].split(","))
    mx = max(mx,b)
    for coord in coords[1:]:
        x,y = map(int, coord.split(","))
        xx,yy = x, y
        if xx != a:
            if a > xx:
                a, xx = xx, a
            for i in range(a, xx+1):
                grid.add((i,b))
        elif yy != b:
            if b > yy:
                b, yy = yy, b
            for i in range(b, yy+1):
                grid.add((a,i))

        a = x
        b = y
        mx = max(mx,y)

for i in range(1000):
    grid.add((i,mx+2))
ans = 0
for i in range(100000):
    x = 500
    y = 0
    for _ in range(1000):

        if (x,y+1) in grid:
            if (x-1, y+1) not in grid:
                x -= 1
                y += 1
            elif (x+1, y+1) in grid:
                if (x,y) not in grid:
                    ans += 1
                    grid.add((x,y))
                break
            else:
                x += 1
                y += 1
        else:
            y += 1

print(ans)