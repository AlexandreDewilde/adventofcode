with open(f"input_5_2022.txt") as f:
    content = f.read()
    lines = content.splitlines()

stacks =  [[] for _ in range(9)]
second_block_idx = 0

for i, line in enumerate(lines):
    if line[1] == '1':
        second_block_idx = i + 2
        break

    if '[' in line:
        for idx, j in enumerate(range(1, len(line), 4)):
            if line[j] == ' ':
                continue
            stacks[idx].append(line[j])

for i in range(len(stacks)):
    stacks[i].reverse()


for i in range(second_block_idx, len(lines)):
    _, cnt, _, fr,  _, to = lines[i].split()
    cnt = int(cnt)
    fr = int(fr) - 1
    to = int(to) - 1

    #part 1
    # for _ in range(cnt):
    #     stacks[to].append(stacks[fr].pop())

    #part 2
    stacks[to].extend(stacks[fr][-cnt:])
    stacks[fr] = stacks[fr][:-cnt]
    
print("".join(stacks[i][-1] for i in range(len(stacks))))