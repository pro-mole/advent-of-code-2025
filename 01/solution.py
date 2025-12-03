#!/usr/local/bin/python3
DEBUG = False

# PART 1
seq = []
with open("input", "r") as input:
    seq = input.readlines()

password = 0

dial = 50

if DEBUG:
    print(f"{dial}")

for step in seq:
    dir = step[0]
    turn = int(step[1:])
    
    dial = (dial + (1 if dir == "R" else -1) * turn) % 100
    if dial == 0:
        password += 1
    if DEBUG:
        print(f"--{turn}-> {dial}")

print(f"Solution 1: {password}")

# PART 2
password = 0

dial = 50

if DEBUG:
    print(f"{dial}")

for step in seq:
    dir = step[0]
    turn = int(step[1:])

    if turn >= 100:
        if DEBUG: print(f"=={turn}==")
        password += turn // 100
        turn = turn % 100

    # Corner case: already at 0 and going back
    if (dial == 0 and dir == "L"):
        dial = 100
    dial = dial + (1 if dir == "R" else -1) * turn
    if DEBUG:
        if dir == "R": print(f"--{turn}-> {dial} [{dial % 100}]")
        if dir == "L": print(f"<-{turn}-- {dial} [{dial % 100}]")
    if dial <= 0 or dial >= 100:
        password += 1
        dial = dial % 100 
        if DEBUG: print(password)
    
print(f"Solution 2: {password}")