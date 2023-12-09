content = open("input.txt").read()

from functools import cmp_to_key


lines = list(map(lambda x: x.split(), content.splitlines()))
ans = 0

    
order = "J23456789TQKA"

def cmp3(x, y):
    if x[1] == y[1]:
        return order.index(x[0]) - order.index(y[0])
    return x[1] - y[1]
def cmp2(x, y):
    x = x[0]
    y = y[0]

    lst1 = [[el, x.count(el)] for el in x]
    lst2 = [[el, y.count(el)] for el in y]

    lst1.sort(key=cmp_to_key(cmp3), reverse=True)
    lst2.sort(key=cmp_to_key(cmp3), reverse=True)
    b1 = "A"
    c1 = 0
    for e, c in lst1:
        if e != "J":
            b1 = e
            c1 = c
            break 
    j1 = x.count("J")
    for i in range(5):
        if lst1[i][0] == "J":
            lst1[i][0] = b1
            lst1[i][1] = c1 + j1
        if b1 == lst1[i][0]:
            lst1[i][1] = c1 + j1
    b1 = "A"
    c1 = 0
    for e, c in lst2:
        if e != "J":
            b1 = e
            c1 = c
            break 
    j1 = y.count("J")
    for i in range(5):
        if lst2[i][0] == "J":
            lst2[i][0] = b1
            lst2[i][1] = c1 + j1
        if lst2[i][0] == b1:
            lst2[i][1] = c1+ j1
    lst1.sort(key=cmp_to_key(cmp3), reverse=True)
    lst2.sort(key=cmp_to_key(cmp3), reverse=True)
    for (e1, c1), (e2, c2) in zip(lst1, lst2):
        if c1 != c2:
            return c1 - c2
    for e1, e2 in zip(x, y):
        if e1 != e2:
            return order.index(e1) - order.index(e2)
    return 0

lines.sort(key=cmp_to_key(cmp2))

print(lines)
ans = sum((i+1)*int(el[1]) for i, el in enumerate(lines))
print(ans)