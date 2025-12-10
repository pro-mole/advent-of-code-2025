#!/usr/local/bin/python3
DEBUG = False
INPUT_FILENAME = "input"

beams = set()
splitters = []
if DEBUG:
    line_size = 0

with open(INPUT_FILENAME, "r") as input:
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

# Part 2 seems to be Dynamic Programming...
# Recursive implementation
def timeline_splits(round_table, start_row, start_pos, memo={}):
    if not (start_row, start_pos) in memo:
        if start_row >= len(round_table)-1:
            memo[(start_row, start_pos)] = 1
        else:
            next_row = round_table[start_row+1]
            if start_pos in next_row:
                memo[(start_row, start_pos)] = timeline_splits(round_table, start_row + 1 , start_pos - 1, memo) + timeline_splits(round_table, start_row + 1 , start_pos + 1, memo)
            else:
                memo[(start_row, start_pos)] = timeline_splits(round_table, start_row + 1, start_pos, memo)
        
    return memo[(start_row, start_pos)]

timelines = 0

with open(INPUT_FILENAME, "r") as input:
    start_line = input.readline()
    timelines = timeline_splits(splitters, 0, start_line.find('S'))

print(f"Part 2 Solution: {timelines}")
