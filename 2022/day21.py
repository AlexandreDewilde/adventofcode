with open(0) as f:
	content = f.read().strip()
	lines = content.splitlines()
    
monkeys = {}
for line in lines:
    k, val = line.split(": ")
    monkeys[k] = val
mk = monkeys.copy()
keys = [0,0]
def calc(monkey):

    if monkeys[monkey].isnumeric():
        return monkeys[monkey]

    k1, k2 = monkeys[monkey][:4], monkeys[monkey][-4:]
    val1, val2 = calc(k1), calc(k2)

    monkeys[monkey] = str(eval(monkeys[monkey].replace(k1,val1).replace(k2,val2)))
    return monkeys[monkey]

calc("root")
print(monkeys["root"])
monkeys = mk
def calc2(monkey):
    if monkey == "humn":
        return "x"
    if monkeys[monkey].isnumeric():
        return monkeys[monkey]
    

    k1, k2 = monkeys[monkey][:4], monkeys[monkey][-4:]
    val1, val2 = calc2(k1), calc2(k2)

    if monkey == "root":
        keys[0] = k1
        keys[1] = k2
    monkeys[monkey] = "(" + str(monkeys[monkey].replace(k1,val1).replace(k2,val2)) + ")"
    return monkeys[monkey]

calc2("root")
eq1 = monkeys[keys[0]]
eq2 = monkeys[keys[1]]

if "x" in eq1:
    equal_to = eval(eq2)
    lo = 0
    hi = int(1e18)
    while lo < hi:
        mid = lo + (hi-lo)//2
        res = eval(eq1.replace("x", str(mid))) - equal_to
        if res == 0:
            print(mid)
            break
        if res < 0:
            hi = mid
        else:
            lo = mid