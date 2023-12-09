import requests
import os
day = "8"
year = "2023"

def get_example(day,offset=0):
    req = requests.get(f'https://adventofcode.com/{year}/day/{day}', headers={'cookie':'session='+os.environ["SESSION_AOC"]})
    return req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]

def submit(day, level, answer):
    input(f'You are about to submit the follwing answer:\n>>>>>>>>>>>>>>>>> {answer}\nPress enter to continue or Ctrl+C to abort.')
    data = {
      'level': str(level),
      'answer': str(answer)
    }

    response = requests.post(f'https://adventofcode.com/{year}/day/{day}/answer', headers={'cookie':'session='+os.environ["SESSION_AOC"]}, data=data)
    if 'You gave an answer too recently' in response.text:
        print('VERDICT : TOO MANY REQUESTS')
    elif 'not the right answer' in response.text:
        if 'too low' in response.text:
            print('VERDICT : WRONG (TOO LOW)')
        elif 'too high' in response.text:
            print('VERDICT : WRONG (TOO HIGH)')
        else:
            print('VERDICT : WRONG (UNKNOWN)')
    elif 'seem to be solving the right level.' in response.text:
        print('VERDICT : INVALID LEVEL')
    else:
        print('VERDICT : OK !')
    

content = ""
file = "sample.txt"
file = "input.txt"

if not os.path.exists(file):
    cookies = {"session": os.environ["SESSION_AOC"]}
    content = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",
        cookies=cookies,
        headers={'User-Agent': "Mozilla/5.0 (X11; Linux i686; rv:109.0) Gecko/20100101 Firefox/120.0"}
    ).text
    with open("input.txt", "w") as f:
        f.write(content)
else:
    with open(file) as f:
        content = f.read()



# content = get_example(day, 2)

lines = content.splitlines()
ans = 0

seq = lines[0]

class Node:
    def __init__(self, name):
        self.name = name
        self.l = None
        self.r = None

match = {}
currents = []
for line in lines[2:]:
    x, _ = line.split(" = ")
    match[x] = Node(x)
    if x[-1] == "A":
        currents.append(match[x])

for line in lines[2:]:
    x, y = line.split(" = ")
    l, r = y.split(", ")
    l = l[1:]
    r = r[:-1]
    match[x].l = match[l]
    match[x].r = match[r]


ends = []
for current in currents:
    end = 0
    for i in range(1000000):
        if current.name[-1] == "Z":
            end = i
            break
        char = seq[i%len(seq)]
        if char == "L":
            current = current.l
        else:
            current = current.r
    ends.append(end)

from math import lcm
current = ends[0]
for end in ends:
    current = lcm(current, end)

ans = current
print(ans)
# submit(day, 1, ans)
submit(day, 2, ans)