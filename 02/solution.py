#!/usr/local/bin/python3
import math

DEBUG = True

seq = []
with open("input", "r") as input:
    seq = input.read().split(",")

invalid_sum = 0

for _range in seq:
    _from, _to = _range.split("-")
    for id in range(int(_from), int(_to)+1):
        str_id = str(id)
        len_id = len(str_id)
        if len_id % 2 == 0:
            halfway = len_id//2
            if str_id[:halfway] == str_id[halfway:]:
                invalid_sum += id

print(f"Part 1 - Solution: {invalid_sum}")

def has_repeats(number_str):
    length = len(number_str)
    if length == 1:
        return False
    
    for size in range(1, (length//2)+1):
        if len(number_str) % size != 0:
            continue

        pattern = number_str[:size]
        repeats = True
        for i in range(1, length // size):
            if pattern != number_str[size*i:size*(i+1)]:
                repeats = False
                break
        
        if repeats: return True

    return False

invalid_sum = 0

for _range in seq:
    _from, _to = _range.split("-")
    for id in range(int(_from), int(_to)+1):
        if has_repeats(str(id)):
            if DEBUG: print(id)
            invalid_sum += id

print(f"Part 2 - Solution: {invalid_sum}")