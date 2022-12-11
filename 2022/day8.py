nb = []
with open(f"input_8_2022.txt") as f:
    content = f.read()
    lines = content.splitlines()
    for line in lines:
        numbers = list(map(int, line))
        nb.append(numbers)
    
mx = 0
for i in range(1,len(nb)-1):
    for j in range(1, len(nb)-1):
        score = 1
        n = 0
        for ii in range(i-1, -1, -1):
            if nb[i][j] <= nb[ii][j]:
                break
        score *= max(1, i -ii)
        for ii in range(i+1, len(nb)):
            if nb[i][j] <= nb[ii][j]:
                break
        score *= max(1, ii-i)
        for jj in range(j+1, len(nb)):
            if nb[i][j] <= nb[i][jj]:
                break
        score *= max(1, jj-j)
        for jj in range(j-1, -1, -1):
            if nb[i][j] <= nb[i][jj]:
                break
        score *= max(1, j-jj)

        mx = max(score, mx)
print(mx)
