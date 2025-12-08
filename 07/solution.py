#!/usr/local/bin/python3
DEBUG = False

beams = set()
splitters = []
if DEBUG:
    line_size = 0

with open("input", "r") as input:
    start_line = input.readline()
    beams.add(start_line.find('S'))
    if DEBUG: line_size = len(start_line)-1

    line = input.readline()
    while len(line) > 0:
        splitters.append(set())
        for i in range(len(line)):
            if line[i] == "^":
                splitters[-1].add(i)
        line = input.readline()    

# Simulate the beam splitting
splits = 0
for round in splitters:
    next = set()
    for beam in beams:
        if beam in round:
            next.add(beam-1)
            next.add(beam+1)
            splits += 1
        else:
            next.add(beam)
    beams = next

    if DEBUG:
        line = ""
        for i in range(line_size):
            line += "|" if i in beams else "."
        print(line)

print(f"Part 1 Solution: {splits}")
