content = ""
from z3 import Solver, Real

ans = 0
lines = content.splitlines()
grid = [list(line) for line in lines]

X = Real("X")
Y = Real("Y")
Z = Real("Z")

VX = Real("VX")
VY = Real("VY")
VZ = Real("VZ")

solver = Solver()
for i, line in enumerate(lines):
	coord, velo = line.split(" @ ")
	x, y, z = map(int, coord.split(", "))
	vx, vy, vz = map(int, velo.split(", "))
	t = Real(f"T{i}")

	solver.add(X + VX * t == x + vx * t)
	solver.add(Y + VY * t == y + vy * t)
	solver.add(Z + VZ * t == z + vz * t)

solver.check()
m = solver.model()
print(m[X].as_long() + m[Y].as_long() + m[Z].as_long())