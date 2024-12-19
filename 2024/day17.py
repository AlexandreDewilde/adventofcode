from aoctools import *
from functools import cmp_to_key
import random
from collections import deque
import heapq

aocd = AOCD(2024, 17)
puzzle_input = aocd.as_str
ans = 0

# puzzle_input = """ """

reg, prog = puzzle_input.split("\n\n")

prog = list(map(int, prog.split(": ")[1].split(",")))
register = {}
reg = reg.split("\n")
for r in reg:
    r = r.split(": ")
    register[r[0].split( )[1]] = int(r[1])

def run(register):
    def combo(x):
        if x <= 3:
            return x
        if x == 4:
            return register["A"]
        if x == 5:
            return register["B"]
        if x == 6:
            return register["C"]

    ip = 0
    def res(opcode, operand, ip, ret):
        if opcode == 0:
            register['A'] = register["A"] // 2**combo(operand)
        elif opcode == 1:
            register["B"] = register["B"] ^ operand

        elif opcode == 2:
            register["B"] = combo(operand) % 8

        elif opcode == 3 and register["A"] != 0:
            ip = operand - 2
        elif opcode == 4:
            register["B"] = register["B"] ^ register["C"]
        elif opcode == 5:
            out = combo(operand) % 8
            ret += str(out) + ","
        elif opcode == 6:
            register["B"] = register["A"] // 2**combo(operand)
        elif opcode == 7:
            register["C"] = register["A"] // 2**combo(operand)
        return ip, ret
    ip = 0
    ret = ""
    while ip < len(prog):
        opcode = prog[ip]
        operand = prog[ip+1]
        ip, ret = res(opcode, operand, ip, ret)
        ip += 2
    return ret

# ans = run(register)[:-1]

cnt = 0
prev = 0
def step2(A, B, C, step=2, initA=None):
    A = A // 2 ** 3
    if A == 0:
        return
    B = A % 8
    B ^= 2
    C = A // 2 ** B
    B = B ^ 3
    B = B ^ C
    if B % 8 == {2: 4, 3: 1, 4: 2, 5: 7, 6: 5, 7: 1, 8:3, 9: 4, 10: 4, 11: 5, 12: 5, 13: 0, 14: 3, 15: 3, 16: 0}[step]:
        if step == 15:
            global prev
            print(initA - prev)
            global cnt
            prev = initA
            cnt += 1
            return
        step2(A, B, C, step+1, initA=initA)

init = 6995444
loop = [33554432,
 33554432,
 524288,
 33030144,
 33554432,
 33554432,
 655360,
 131072,
 12451840,
 195584,
 1024,
 20119552,
524288,
33030144,
33554432]
prev = 0
current = init
# for i in range(1000000000):
#     initA = current
#     A = current
#     B = A % 8
#     B ^= 2
#     C = A // 2 ** B
#     B = B ^ 3
#     B = B ^ C
#     if B % 8 == 2:
#         # print(initA, initA - prev)
#         # prev = initA
#         step2(A, B, C, initA=initA)l
#     current += loop[i % len(loop)]
init = 37222273957364
loop = [524288,
140737487831040]


current = init

for i in range(1000000000):
    register["A"] = current
    pr = list(map(int, (run(register)[:-1].split(","))))
    print(pr, current)
    if pr == prog:
        ans = current
        break
    if i % 100000 == 0:
        print(i)
    current += loop[i % len(loop)]
input()
aocd.p1(ans)
input()
aocd.p2(ans)