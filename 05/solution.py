#!/usr/local/bin/python3
DEBUG = False

fresh_ranges = []
ingredients = []
with open("input", "r") as input:
    range_str = input.readline().strip()
    while len(range_str) > 0:
        fresh_ranges.append(tuple([int(x) for x in range_str.split("-")]))
        range_str = input.readline().strip()
    
    ingredients = [int(x) for x in input.readlines()]

fresh_ranges.sort()

optimized_ranges = []
for f_range in fresh_ranges:
    if DEBUG: print(f_range)
    skip = False
    for i in range(len(optimized_ranges)):
        e_range = optimized_ranges[i]
        # Merge ranges in one check instead of doing all cases individually
        if (f_range[0] >= e_range[0] and f_range[0] <= e_range[1]) or (f_range[1] >= e_range[0] and f_range[1] <= e_range[1]) or (e_range[0] >= f_range[0] and e_range[0] <= f_range[1]) or (e_range[1] >= f_range[0] and e_range[1] <= f_range[1]):
            skip = True
            optimized_ranges[i] = (min(f_range[0],e_range[0]), max(f_range[1],e_range[1]))
            if DEBUG: print(f"Ranges {f_range} and {e_range} fused as {optimized_ranges[i]}")
            break
    
    if not skip: optimized_ranges.append(f_range)
    # if DEBUG: print(optimized_ranges)

fresh = 0

for ingredient in ingredients:
    for fresh_range in optimized_ranges:
        if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
            fresh += 1
            break

print(f"Part 1 Solution: {fresh}")

fresh_stuff = 0

# This is a crude solution, but it does work
# It is *unlikely* that the solution is so big an array cannot contain it
# If that is the case, then I will have to go back and optimize the ranges list...
for fresh_range in optimized_ranges:
    fresh_stuff += fresh_range[1] - fresh_range[0] + 1

print(f"Part 2 Solution: {fresh_stuff}")