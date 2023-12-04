import requests
import os

content = ""
file = "sample.txt"
file = "input.txt"

if not os.path.exists(file):
    cookies = {"session": os.environ["SESSION_AOC"]}
    content = requests.get("https://adventofcode.com/2023/day/4/input",
        cookies=cookies,
        headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0"}
    ).text
    with open("input.txt", "w") as f:
        f.write(content)
else:
    with open(file) as f:
        content = f.read()


# content = ""
# for _ in range(10):
#     content += input() + "\n"
# content = content[:-1]

lines = content.splitlines()



ans = [1] * len(lines)
for line in  lines:
    nb,lst = line.split(":")

    lst, winning = lst.split(" | ")

    winning = set(winning.split(" "))

    matching = 0
    for number in lst.split():
        if number in winning:
            matching += 1
        
    nb = int(nb.split()[-1]) - 1
    for i in range(nb+1, min(len(lines), nb + matching+1)):
        ans[i] += 1 * ans[nb]

print(sum(ans))
