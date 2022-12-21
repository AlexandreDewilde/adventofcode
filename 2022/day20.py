from collections import deque

class Node:
	def __init__(self, val=None):
		self.val = val
	
with open(0) as f:
	content = f.read().strip()
	lines = content.splitlines()

	nb = list(map(lambda x:Node(int(x)*811589153), list(lines)))

dq = deque(nb)
for _ in range(10):
	for i,n in enumerate(nb):

		while dq[0] != n:
			dq.append(dq.popleft())
		p = dq.popleft()

		idx = p.val
		if idx > len(dq):
			idx %= len(dq)
		if idx < 0:
			idx = abs(idx)
			if idx > len(dq):
				idx %= len(dq)
			idx = len(dq) - idx
		dq.insert(idx, p)
	
while dq[0].val != 0:
	dq.append(dq.popleft())

print(dq[1000%len(nb)].val+dq[2000%len(nb)].val+dq[3000%len(nb)].val)