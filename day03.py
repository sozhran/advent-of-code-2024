# DAY 3

# Preparation

import re

with open('./inputs/day03.txt', 'r') as file:
    input = file.read()

def match_finder(data: str):
    final_result = 0

    regexp_for_instructions = r"mul\([0-9]+,{1}[0-9]+\)"

    list_of_matches = re.findall(regexp_for_instructions, data)

    for instruction in list_of_matches:
        reg1 = r"(?<=mul\()[0-9]+(?=,)"
        reg2 = r"(?<=,)[0-9]+(?=\))"
        a = re.search(reg1, instruction).group()
        b = re.search(reg2, instruction).group()

        final_result += (int(a) * int(b))
    
    return final_result

# Part 1

print("Result: ", match_finder(input))

# Part 2
# There's a truly beautiful solution on Reddit which I accidentially spoiled for myself,
# but I found my own out of sheer principle.

corrected_input = input.split('do()')
corrected_result = 0

for item in corrected_input:
    new = item.split("don't()")
    corrected_result += match_finder(new[0])

print(corrected_result)
