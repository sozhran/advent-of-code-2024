# DAY 4

# Preparation

from re import findall

with open('./inputs/day04.txt', 'r') as file:
    input = file.read().split('\n')

for line in input:
    if not line:
        input.remove(line)

max_line_length = max([len(x) for x in input])

# FUNCTIONS

def match_finder(data: str):
    xmas_matches = findall(r"XMAS", data)
    samx_matches = findall(r"SAMX", data)

    return len(xmas_matches) + len(samx_matches)

# Part 1

match_counter = 0

for horizontal_line in input:
    match_counter += match_finder(horizontal_line)

for x in range(max_line_length):
    vertical_line = [input[y][x] if input[y][x] else '' for y in range(len(input))]
    vertical_line_as_string = ''.join(vertical_line)
    match_counter += match_finder(vertical_line_as_string)    

for y in range(len(input) - 3):
    for x in range(max_line_length - 3):
        match_counter += match_finder(str(input[y][x] + input[y+1][x+1] + input[y+2][x+2] + input[y+3][x+3]))
        match_counter += match_finder(str((input[y][x+3] + input[y+1][x+2] + input[y+2][x+1] + input[y+3][x])))

print("Part 1 answer: ", match_counter)

# Part 2

cross_match_counter = 0

for y in range(len(input) - 2):
    for x in range(max_line_length - 2):
        string1 = str(input[y][x] + input[y+1][x+1] + input[y+2][x+2])
        string2 = str(input[y][x+2] + input[y+1][x+1] + input[y+2][x])
        
        if string1 in ("MAS", "SAM") and string2 in ("MAS", "SAM"):
            cross_match_counter += 1            

print("Part 2 answer: ", cross_match_counter)