with open("input_1_2022.txt") as f:
    blocks = f.read().split("\n\n")

# task 1
ans = 0
for block in blocks:
    s = sum(map(int, block.splitlines()))
    ans = max(ans, s)
print(ans)


#task 2
ans = []
for block in blocks:
    s = sum(map(int, block.splitlines()))
    ans.append(s)
ans.sort()
print(sum(ans[-3:]))

#one liner
#print(sum(sorted([sum(map(int, block.splitlines())) for block in open("input_1_2022.txt").read().split("\n\n")])[-3:]))
