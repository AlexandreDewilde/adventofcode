
with open(0) as f:
	content = f.read()
	lines = content.splitlines()
	
length = float("inf")
for line in lines[:-2]:
	length = min(length, len(line.strip()))

g = lines[:-2]
actions = lines[-1] + " "

cubes = [[["@"]*length for _ in range(length)] for _ in range(6)]

def display(cube):
	for line in cubes[cube]:
		print("".join(line))
done = 0
done_cubes = 0
opened = set()
start = None
for i, line in enumerate(g):
	jj = 0
	for j, char in enumerate(line):
		if char == " ": continue
		if start is None:
			start = (i%length, jj%length)
		try:cubes[done_cubes+jj//length][i%length][jj%length] = char
		except:pass
		done += 1
		jj += 1
	if (i+1) % length == 0:
		done_cubes += len(line.strip()) // length

current = 0
direction = (0,1)
pos = start
cube = 0
for char in actions[:]:
	if char.isnumeric():
		current = current*10 + int(char)
		continue
	for i in range(current):
		prev_cube = cube
		prev_dir = direction
		new_pos = (pos[0]+direction[0], pos[1]+direction[1])
		if cube == 0:
			if new_pos[1] < 0:
				new_pos = (length-pos[0]-1, 0)
				cube = 3
				direction = (0, 1)
			elif new_pos[1] >= length:
				new_pos = (pos[0], 0)
				cube = 1
			elif new_pos[0] < 0:
				cube = 5
				new_pos = (pos[1], 0)
				direction = (0,1)
			elif new_pos[0] >= length:
				new_pos = (0, pos[1])
				cube = 2
		elif cube == 1:
			if new_pos[0] < 0:
				cube = 5
				new_pos = (length-1, pos[1])
			elif new_pos[0] >= length:
				cube = 2
				direction = (0, -1)
				new_pos = (pos[1], length-1)
			elif new_pos[1] < 0:
				cube = 0
				new_pos = (pos[0], length-1)
			elif new_pos[1] >= length:
				cube = 4
				direction = (0, -1)
				new_pos = (length-1-pos[0], length-1)
		elif cube == 2:
			if new_pos[0] < 0:
				cube = 0
				new_pos = (length-1, pos[1])
			elif new_pos[0] >= length:
				cube = 4
				new_pos = (0, pos[1])
			elif new_pos[1] < 0:
				cube = 3
				new_pos = (0, pos[0])
				direction = (1, 0)
			elif new_pos[1] >= length:
				cube = 1
				direction = (-1, 0)
				new_pos = (length-1, pos[0])
		elif cube == 3:
			if new_pos[0] < 0:
				cube = 2
				direction = (0,1)
				new_pos = (pos[1], 0)
			elif new_pos[0] >= length:
				cube = 5
				new_pos = (0, pos[1])
			elif new_pos[1] < 0:
				cube = 0
				new_pos = (length-1-pos[0], 0)
				direction = (0, 1)
			elif new_pos[1] >= length:
				cube = 4
				new_pos = (pos[0], 0)
		elif cube == 4:
			if new_pos[0] < 0:
				cube = 2
				new_pos = (length-1, pos[1])
			elif new_pos[0] >= length:
				cube = 5
				new_pos = (pos[1], length-1)
				direction = (0,-1)
			elif new_pos[1] < 0:
				cube = 3
				new_pos = (pos[0], length-1)
			elif new_pos[1] >= length:
				cube = 1
				direction = (0, -1)
				new_pos = (length-1-pos[0], length-1)
		else:
			if new_pos[0] < 0:
				cube = 3
				new_pos = (length-1, pos[1])
			elif new_pos[0] >= length:
				cube = 1
				new_pos = (0, pos[1])
			elif new_pos[1] < 0:
				cube = 0
				direction = (1, 0)
				new_pos = (0, pos[0])
			elif new_pos[1] >= length:
				cube = 4
				direction = (-1, 0)
				new_pos = (length-1, pos[0])
		if cubes[cube][new_pos[0]][new_pos[1]] == ".":
			pos = new_pos
		else:
			cube = prev_cube
			direction = prev_dir
			break
	
	
	print(cube, pos, direction)
	# print(char,current)
	# # display(cube)
	# print()
	if char == " ":
		break
	current = 0
	if direction == (1,0):
		if char == "L":
			direction = (0,1)
		else:
			direction = (0,-1)
	elif direction == (-1,0):
		if char == 'L':
			direction = (0,-1)
		else:
			direction = (0,1)
	elif direction == (0,1):
		if char == "L":
			direction = (-1,0)
		else:
			direction = (1,0)
	else:
		if char == "L":
			direction = (1,0)
		else:
			direction = (-1,0)

val_orientation = {(0,1):0, (0,-1):3, (-1,0):1, (0,-1):2}
cbs_inc = {0: (0,50), 1:(0,100), 2: (50,50), 3: (100,0), 4:(100,50), 5:(150,0)}
print(cube, pos, direction)

print((cbs_inc[cube][0]+pos[0]+1)*1000+(cbs_inc[cube][1] + pos[1]+1)*4+2)