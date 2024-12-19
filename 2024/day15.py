from aoctools import *
from functools import cmp_to_key

aocd = AOCD(2024, 15)
puzzle_input = aocd.as_str
ans = 0


# puzzle_input = """##########
# #..O..O.O#
# #......O.#
# #.OO..O.O#
# #..O@..O.#
# #O#..O...#
# #O..O..O.#
# #.OO.O.OO#
# #....O...#
# ##########

# <vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
# vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
# ><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
# <<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
# ^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
# ^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
# >^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
# <><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
# ^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
# v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

# puzzle_input = """#######
# #...#.#
# #.....#
# #..OO@#
# #..O..#
# #.....#
# #######

# <vv<<^^<<^^"""

g, moves = puzzle_input.split("\n\n")
grid = [list("".join("[]" if el == "O" else el * 2 for el in line)) for line in g.splitlines()]

start = None
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "@":
            print(i, j)
            grid[i][j] = "."
            grid[i][j + 1] = "."
            start = (i, j)
            break

def check(current, nxt, to_move, prev="."):
    if grid[current[0]][current[1]] == "#":
        return False

    to_move[current] = prev
    if grid[current[0]][current[1]] == "[":
        ret = check((current[0] + nxt[0], current[1] + nxt[1]), nxt, to_move, prev="[")
        if nxt[0] != 0:
            if (current[0], current[1] + 1) not in to_move:
                to_move[(current[0], current[1] + 1)] = "."
            ret = ret and check((current[0] + nxt[0], current[1] + nxt[1] + 1), nxt, to_move, prev="]")
        return ret
    if grid[current[0]][current[1]] == "]":
        ret = check((current[0] + nxt[0], current[1] + nxt[1]), nxt, to_move, prev="]")
        if nxt[0] != 0:
            if (current[0], current[1] - 1) not in to_move:
                to_move[(current[0], current[1] - 1)] = "."
            ret = ret and check((current[0] + nxt[0], current[1] + nxt[1] - 1), nxt, to_move, prev="[")
        return ret

    return True

current = start
for move in moves:
    # for line in grid:
    #     print("".join(line))
    # input()
    nxt = None
    if move == ">":
        nxt = (0, 1)
    elif move == "<":
        nxt = (0, -1)
    elif move == "^":
        nxt = (-1, 0)
    elif move == "v":
        nxt = (1, 0)
    elif move == "\n":
        continue

    # if not (0 <= current[0] + nxt[0] < len(grid) and 0 <= current[1] + nxt[1] < len(grid[0])):
    #     continue
    if grid[current[0] + nxt[0]][current[1] + nxt[1]] == "#":
        continue

    # later = (current[0] + nxt[0], current[1] + nxt[1])
    # future = []
    # while grid[later[0]][later[1]] == "O":
    #     later = (later[0] + nxt[0], later[1] + nxt[1])
    #     future.append(later)

    # if grid[later[0]][later[1]] == ".":
    #     current = (current[0] + nxt[0], current[1] + nxt[1])
    #     grid[current[0]][current[1]] = "."
    #     for f in future:
    #         grid[f[0]][f[1]] = "O"

    future = {}
    if check((current[0] + nxt[0], current[1] + nxt[1]), nxt, future):
        print(future    )
        for coord, nc in future.items():
            grid[coord[0]][coord[1]] = nc
        current = (current[0] + nxt[0], current[1] + nxt[1])

for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "[":
            ans += 100 * i + j

print(ans)
# input()
# aocd.p1(ans)
input()
aocd.p2(ans)