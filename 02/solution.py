#!/usr/local/bin/python3

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