content = ""
ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]


segments = []
for line in lines:
	coord, velo = line.split(" @ ")
	x, y, z = map(int, coord.split(", "))
	vx, vy, vz = map(int, velo.split(", "))

	segments.append((vy / vx, y - vy / vx * x, x, y, vx, vy))

def check(a, inter, y):
	if a[4] >= 0:
		if inter < a[2]:
			return False
	else:
		if inter > a[2]:
			return False
	if a[5] >= 0:
		if y < a[3]:
			return False
	else:
		if y > a[3]:
			return False
	return True
def sign(x):
	return 1 if x >= 0 else -1
def cmp_inter(a, b):
	if b[0] == a[0]:
		return b[1] == a[1]
	inter = - (b[1] - a[1]) / (b[0] - a[0])
	y = a[0] * inter + a[1]
	left = 200000000000000
	right = 400000000000000
	if not check(a, inter, y) or not check(b, inter, y):
		return False
	if left <= inter <= right and left <= y <= right:
		print(inter, y, a[2], a[3])
		return True
	return False

for i in range(len(segments)):
	for j in range(i + 1, len(segments)):
		if cmp_inter(segments[i], segments[j]):
			ans += 1
print(ans)
