with open(f"input") as f:
    lines = f.readlines()

overlap = []
for line in lines:
    a,b = line.split(',')
    a = tuple(map(int, a.split("-")))
    b = tuple(map(int, b.split("-")))
    overlap.append((a,b))


#task 1
ans = 0
for a,b in overlap:
    if b[0] <= a[0] <= a[1] <= b[1] or a[0] <= b[0] <= b[1] <= a[1]:
        ans += 1
print(ans)

#task 2
ans = 0
for a,b in overlap:
    if b[0] <= a[0] <= b[1] or a[0] <= b[0] <= a[1]:
        ans += 1
print(ans)