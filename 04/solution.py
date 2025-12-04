#!/usr/local/bin/python3
DEBUG = False

map = []
with open("./input", "r") as input:
    for line in input.readlines():
        map.append(line.strip())

rolls = 0

w = len(map[0])
h = len(map)

y = 0
for line in map:
    x = 0
    for char in line:
        if char == "@":
            adj = 0
            for dy in [-1,0,1]:
                for dx in [-1,0,1]:
                    if dx == 0 and dy == 0:
                        continue
                    if x + dx < 0 or x + dx >= w or y + dy < 0 or y + dy >= h:
                        continue
                    if map[y+dy][x+dx] == "@":
                        adj += 1
                    if adj >= 4:
                        break
            if adj < 4:
                rolls += 1
                if DEBUG: print(f"{x},{y} : {adj}")
        x += 1
    y += 1

print(f"Part 1 Solution: {rolls}")

rolls = 0
drolls = []

w = len(map[0])
h = len(map)

while(True):
    y = 0
    for line in map:
        x = 0
        for char in line:
            if char == "@":
                adj = 0
                for dy in [-1,0,1]:
                    for dx in [-1,0,1]:
                        if dx == 0 and dy == 0:
                            continue
                        if x + dx < 0 or x + dx >= w or y + dy < 0 or y + dy >= h:
                            continue
                        if map[y+dy][x+dx] == "@":
                            adj += 1
                        if adj >= 4:
                            break
                if adj < 4:
                    drolls.append((x,y))
                    if DEBUG: print(f"{x},{y} : {adj}")
            x += 1
        y += 1
    
    if len(drolls) == 0: break
    rolls += len(drolls)
    if DEBUG: print(drolls)
    for (rollx,rolly) in drolls:
        map[rolly] = map[rolly][:rollx] + "." + map[rolly][rollx+1:]
    drolls = []

    if DEBUG:
        for line in map: print(line)

print(f"Part 2 Solution: {rolls}")
