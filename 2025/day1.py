with open("input") as f:
    lines = f.read()


current = 50
ans = 0
for line in lines.split("\n")[:-1]:
    line = line.strip()
    direction, value = line[0], int(line[1:])
    ans += value // 100
    value %= 100
    if direction == "L":
        value *= -1
    prev = current

    current = (current + value) % 100
    if prev == 0:
        pass

    elif value > 0 and prev + value >= 100:
        ans += 1
    elif value < 0 and prev + value <= 0:
        ans += 1
    # print(current, axns)
print(ans)
