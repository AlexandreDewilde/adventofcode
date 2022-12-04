with open("input_2_2022.txt") as f:
    content = f.read()
    lines = content.splitlines()


scores_a = {letter : i for i, letter in enumerate("ABC")}
scores_b = {letter : i for i, letter in enumerate("XYZ")}
# part 1
score = 0
for line in lines:

    a, b = line.split()

    score += scores_b[b] + 1
    
    delta = ord(b) - ord(a) - ord("X") + ord("A")
    if delta == 0:
        score += 3
    elif delta == 1 or delta == -2:
        score += 6

print(score)


# part 2
score = 0
for line in lines:

    a, b = line.split()
    score += scores_b[b] * 3
    
    res = scores_a[a] + int(b == "Z") - int(b == "X")

    score += res % 3 + 1
    
    
print(score)