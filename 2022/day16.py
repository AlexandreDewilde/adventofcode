from collections import deque

with open(0) as f:
	content = f.read()
	lines = content.splitlines()
	# lines.append("")
from collections import defaultdict
g = defaultdict(lambda: [])
rates = defaultdict(lambda: [])
mappings = {}
c = 0
for line in lines:
    line += ","
    _, a, _, _, rate, _, _, _, _, *to = line.split()
    rate = int(rate.split("=")[1][:-1])
    if a not in mappings:
        mappings[a] = c
        c += 1
    rates[mappings[a]] = rate
    for t in to:
        b = t[:-1].strip()
        if b not in mappings:
            mappings[b] = c
            c += 1
        g[mappings[a]].append(mappings[b])
        # g[mappings[b]].append(mappings[a])

start = mappings["AA"]

import tqdm
# bar = tqdm.tqdm()
opened = [False]*len(mappings)
mem = {}
target = set()
from functools import cache
@cache
def dfs(i, j, d, dd, current, c2):
    # bar.update(1)
    if d > 26 and dd > 26:
        target.add((i,j,d,dd,current,c2))
        
        return 0
    if (i,j,min(d,27),min(dd,27),current+c2) in mem:

        return mem[(i,j,min(d,27),min(dd,27),current+c2)]
    if (j,i, min(dd, 27), min(d,27), c2+current) in mem:
        return mem[(j,i, min(dd, 27), min(d,27), c2+current)]
    if (j,i, min(d, 27), min(dd,27), current, c2) in mem:
        return mem[(j,i, min(d, 27), min(dd,27), current+c2)]
    if (i,j, min(dd, 27), min(d,27), c2+current) in mem:
        return mem[(i,j, min(dd, 27), min(d,27), c2+current)]
    if (j, i, min(d, 27), min(dd,27), c2+current) in mem:
        return mem[(j, i, min(d, 27), min(dd,27), c2+current)]
    if (i, j, min(dd, 27), min(d,27), current+c2) in mem:
        return mem[(i, j, min(dd, 27), min(d,27), current+c2)]
    ans = 0
    if d > 26:
        for d2 in g[j]:
            res = dfs(i, d2, d+1, dd+1, current, c2) 
            ans = max(ans, res)
            if opened[i] and opened[j]: continue
            if rates[j] and not opened[j] and dd < 25:
                opened[j] = True
                res = (dfs(i, d2, d+1, dd+2, current, c2 + rates[j]))
                res+= rates[j] * (26-dd-2)
                ans = max(ans, res)
                    # p = [current+c2] + path
                opened[j] = False
    elif dd > 26:
        for adj in g[i]:
            res = dfs(adj, j, d+1, dd+1, current, c2) 
            ans = max(ans, res)
            if opened[i] and opened[j]: continue
            if rates[i] and not opened[i] and d < 25:
                opened[i] = True
                res = (dfs(adj, j, d+2, dd+1, current + rates[i], c2))
                res += (26-d-2) * rates[i]
                ans = max(res, ans)
                    # p = [current+c2] + path
                opened[i] = False
    else:
        for adj in g[i]:
            for d2 in g[j]:
                res = dfs(adj, d2, d+1, dd+1, current, c2) 
                ans = max(ans, res)
                if opened[i] and opened[j]: continue
                if rates[i] and not opened[i] and d < 25:
                    opened[i] = True
                    res = (dfs(adj, d2, d+2, dd+1, current + rates[i], c2))
                    res+= (27-d-2)*rates[i]
                    
                    ans = max(res, ans)
                        # p = [current+c2] + path
                    opened[i] = False
                if rates[j] and not opened[j] and dd < 25:
                    opened[j] = True
                    res = (dfs(adj, d2, d+1, dd+2, current, c2 + rates[j]))
                    res += (27-dd-2) * rates[j]
                    ans = max(ans, res)
                        # p = [current+c2] + path
                    opened[j] = False
                if rates[i] and rates[j] and not opened[i] and not opened[j] and i != j and dd <= 24 and d <= 24:
                    opened[i] = True
                    opened[j] = True
                    res = (dfs(adj, d2, d+2, dd+2, current + rates[i], c2+rates[j]))
                    res += (27-dd-2)*rates[j]
                    res += (27-d-2)*rates[i]
                    ans = max(res, ans)
                    opened[i] = False
                    opened[j] = False
    mem[(i,j,min(d,27),min(dd,27),current+c2)] = ans
    return ans
res = (dfs(start, start, 0, 0,0,0))
print(res)