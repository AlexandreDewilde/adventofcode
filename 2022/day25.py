with open(0) as f:
	content = f.read()
	lines = content.splitlines()

res = 0
for line in lines:
    val = 0
    for exp,char in enumerate(line[::-1]):
        if char == "-":
            char = -1
        if char == "=":
            char = -2
        val += int(char) * 5**exp
    res += val

snafu = ""

while res:
    to_add = res % 5
    if to_add == 0:
        snafu += "0"
    elif to_add== 1:
        snafu += "1"
        res -= 1 
    elif to_add== 2:
        snafu += "2"
        res -= 2
    elif to_add == 3:
        snafu += "="
        res += 2
    elif to_add == 4:
        snafu += "-"
        res += 1
    res//= 5
print(snafu[::-1])
