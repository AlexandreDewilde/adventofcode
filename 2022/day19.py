from collections import deque
with open(0) as f:
	content = f.read().strip()
	lines = content.splitlines()
	# lines.append("")

bp = []
for line in lines:
    _, _, _, _, _, _, ore, _, _, _, _, _, clay, *t = line.split()
    # print(ore, clay)
    _, _, _, _, _, obsidian_1, _,_, obsidian_2, *p = t
    # print(obsidian_1, obsidian_2)
    # print(p)
    _, _, _, _, _, geod_1, _, _, geod_2, *e = p
    # print(geod_1, geod_2)
    pattern = (int(ore), int(clay), (int(obsidian_1), int(obsidian_2)), (int(geod_1), int(geod_2)))

    bp.append(pattern)

from functools import cache

@cache
def maximize(ress, robots, bp, it):
    if it >= 24:
        # print(ress, robots)
        return 0
    it += 1
    ress = (ress[0]+robots[0], ress[1]+robots[1], ress[2]+robots[2], ress[3]+ robots[3])
    ans = 0
    if ress[0] >= bp[0]:
        c_ress = (ress[0]-bp[0], ress[1], ress[2], ress[3])
        c_r = (robots[0]+1, robots[1], robots[2], robots[3])
        ans = max(ans, maximize(c_ress, c_r, bp, it))
        # used = True
    if ress[0] >= bp[1]:
        c_ress = (ress[0]-bp[1], ress[1], ress[2], ress[3])
        c_r = (robots[0], robots[1]+1, robots[2], robots[3])
        ans = max(ans, maximize(c_ress, c_r, bp, it))
        # used = True
    if ress[0] >= bp[2][0] and ress[1] >= bp[2][1]:
        c_ress = (ress[0]-bp[2][0], ress[1]-bp[2][1], ress[2], ress[3])
        c_r = (robots[0], robots[1], robots[2]+1, robots[3])
        ans = max(ans, maximize(c_ress, c_r, bp, it))
        # used = True
    if ress[0] >= bp[3][0] and ress[2] >= bp[3][1]:
        c_ress = (ress[0]-bp[3][0], ress[1], ress[2]-bp[3][1], ress[3])
        c_r = (robots[0], robots[1], robots[2], robots[3]+1)
        ans = max(ans, maximize(c_ress, c_r, bp, it)+1)
        # used = True
        
    ans = maximize(ress, robots, bp, it)
    return ans

for b in bp:
    print(maximize((0,0,0,0), (1,0,0,0), b,0))