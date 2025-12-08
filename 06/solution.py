#!/usr/local/bin/python3
DEBUG = False

numbers = []
ops = []

with open("input", "r") as input:
    line = [s.strip() for s in input.readline().split()]
    while len(line) > 0:
        if line[0].isnumeric():
            numbers.append([int(n) for n in line])
        else:
            ops = line
        line = [s.strip() for s in input.readline().split()]

sum_total = 0

for i in range(len(ops)):
    op = ops[i]
    result = 0 if op == '+' else 1
    for numberline in numbers:
        result = (result + numberline[i]) if op == '+' else (result * numberline[i])
    sum_total += result
    if DEBUG:
        print(f"{op.join([str(numberline[i]) for numberline in numbers])} = {result}")

print(f"Part 1 Solution: {sum_total}")
