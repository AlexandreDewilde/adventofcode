import requests
import os

content = ""
if not os.path.exists("input.txt"):
    cookies = {"session": os.environ["SESSION_AOC"]}
    content = requests.get("https://adventofcode.com/2023/day/1/input",
        cookies=cookies,
        headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0"}
    ).text
    with open("input.txt", "w") as f:
        f.write(content)
else:
    with open("input.txt") as f:
        content = f.read()

total = 0
mapping = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
for i in range(len(content.splitlines())):
    nb = []
    line = content.splitlines()[i]
    for i in range(len(line)):
        for word in mapping:
            # print(line[:i], word, line[:i].endswith(word))
            if line[:i+1].endswith(word):
                nb.append(mapping.index(word)+1)
        if line[i].isnumeric():
            nb.append(line[i])
    total += int(str(nb[0]) + str(nb[-1]))
print(total)