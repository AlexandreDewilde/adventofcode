with open(f"input_10_2022.txt") as f:
    content = f.read()
    lines = content.splitlines()


cycle = 0
ans = []
x = 1
for line in lines:
    if line == "noop":
        if abs(cycle%40-x) in {0,1}:
            ans.append("#")
        else:
            ans.append(" ")
        cycle += 1

    else:
        for i in range(2):
            if abs(cycle%40-x) in {0,1}:
                ans.append("#")
            else:
                ans.append(" ")
            cycle += 1
        x += int(line.split()[-1])

for i in range(0,241,40):
    print("".join(ans[i:i+40]))