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

#TODO sort range array so we can stop search below earlier
#TODO join consecutive/intersecting ranges

fresh = 0

for ingredient in ingredients:
    for fresh_range in fresh_ranges:
        if ingredient >= fresh_range[0] and ingredient <= fresh_range[1]:
            fresh += 1
            break

print(f"Part 1 Solution: {fresh}")