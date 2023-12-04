import requests
import os

content = ""
if not os.path.exists("input.txt"):
    cookies = {"session": os.environ["SESSION_AOC"]}
    content = requests.get("https://adventofcode.com/2023/day/2/input",
        cookies=cookies,
        headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0"}
    ).text
    with open("input.txt", "w") as f:
        f.write(content)
else:
    with open("input.txt") as f:
        content = f.read()
# content = ""
# for _ in range(5):
#     content += input() + "\n"
# content = content[:-1]
lines = content.splitlines()

# ints = list(map(int, lines))
# floats = list(map(float, lines))

ans = 0
for line in lines:
    id, line = line.split(":")
    game = [0, 0, 0]
    m = ["blue", "red", "green"]
    mx = [14, 12, 13]
    poss =True
    game = [0,0,0]
    for game_ in line.split("; "):
        game_ = game_.split(", ")
        gamex = [0,0,0]
        for x in game_:
            nb, c = x.strip().split()
            nb = int(nb)
            idx = m.index(c)
            gamex[idx] += nb
        game[0] = max(game[0], gamex[0])
        game[1] = max(game[1], gamex[1])
        game[2] = max(game[2], gamex[2])
    ans += game[0] * game[1] * game[2]
print(ans)