#!/usr/local/bin/python3
DEBUG = False

batteries = []

with open("input", "r") as input:
    batteries = input.readlines()

joltage = 0

for battery in batteries:
    #First step: find the largest number
    battery = battery[:-1]
    if DEBUG: print(battery)

    large_v = 0
    large_i = 0
    i = 0
    for j in battery:
        v = int(j)
        if v > large_v:
            large_i = i
            large_v = v
        i += 1
    
    # Case 1: largest is at the end; get the second largest before and form the number
    if large_i == i-1:
        small_v = 0
        i = 0
        for j in battery:
            if i == large_i:
                break
            v = int(j)
            if v > small_v:
                small_v = v
            i += 1
        if DEBUG: print(f"{small_v}{large_v}")
        joltage += small_v * 10 + large_v
    # Case 2: get the largest number after the first one we found
    else:
        small_v = 0
        i = 0
        for j in battery:
            if i > large_i:
                v = int(j)
                if v > small_v:
                    small_v = v
            i += 1
        if DEBUG: print(f"{large_v}{small_v}")
        joltage += large_v * 10 + small_v

print(f"Part 1 Solution: {joltage}")

joltage = 0

for battery in batteries:
    battery = battery[:-1]
    if DEBUG: print(battery)

    while len(battery) > 12:
        # Remove any number that produces the largest n-1 number among the possibilities
        # This is _probably_ not very efficient, but it should work
        best = "0"
        for i in range(len(battery)):
            candidate = battery[:i] + battery[i+1:]
            if int(best) < int(candidate):
                best = candidate
        battery = best

    if DEBUG: print(battery)
    joltage += int(battery)

print(f"Part 2 Solution: {joltage}")