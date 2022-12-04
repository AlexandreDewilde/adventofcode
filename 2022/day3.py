with open(f"input_3_2022.txt") as f:
    lines = f.read().splitlines()

#task 1
ans = 0
for line in lines:
    mid = len(line) // 2
    commons = set(line[:mid]).intersection(line[mid:])
    
    for common in commons:
        if common.isupper():
            ans += ord(common) - ord("A") + 27
        else:
            ans += ord(common) - ord("a") + 1
print(ans)

#task 2
ans = 0
for i in range(len(lines)//3):
    commons = set(lines[i*3]).intersection(lines[i*3+1]).intersection(lines[i*3+2])
    for common in commons:

        if common.isupper():
            ans += ord(common) - ord("A") + 27
        else:
            ans += ord(common) - ord("a") + 1
            
print(ans)