*rows, operators = open("input").read().strip().split("\n")
# rows = [list(map(str, row.split())) for row in rows]
operators = operators.split()

ans = 0

current_col = 0
for i in range(len(operators)):
    current = 0 if operators[i] == "+" else 1
    # for row in rows:
    #     if operators[i] == "+":
    #         current += int(row[i])
    #     else:
    #         current *= int(row[i])
    while current_col < len(rows[0]) and not all(
        row[current_col] == " " for row in rows
    ):
        number = ""
        for r in range(len(rows)):
            # print(rows[r][current_col], r, current_col)
            if rows[r][current_col] != " ":
                number = number + rows[r][current_col]
        current_col += 1
        if operators[i] == "+":
            current += int(number)
        else:
            current *= int(number)
    current_col += 1
    ans += current
print(ans)
