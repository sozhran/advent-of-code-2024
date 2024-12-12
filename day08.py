# DAY 8

# Preparation

from itertools import count

with open('./inputs/day08.txt', 'r') as file:
    input = file.read().split('\n')

for line in input:
    if not line:
        input.remove(line)

# FUNCTIONS

max_x = len(input[0])
max_y = len(input)

def check_coordinates(x, y):
    check = (0 <= x < max_x) and (0 <= y < max_y)
    return check

# Parts 1 & 2

antennas = {}
result1 = []
result2 = []

for y, line in zip(count(), input):
    for x, char in zip(count(), line):
        if char == ".":
            continue

        if char in antennas.keys():
            antennas[char].append((x, y))
        else:
            antennas[char] = [(x, y)]

for antenna in antennas.keys():
    values = antennas[antenna]
    for i in range (len(values) - 1):
        j = i+1
        
        while j < len(values):
            x1, y1 = values[i][0], values[i][1]
            x2, y2 = values[j][0], values[j][1]

            dx, dy = x2 - x1, y2 - y1
            
            # For part 1:
            if check_coordinates(x1 - dx, y1 - dy):
                result1.append((x1 - dx, y1 - dy))
            if check_coordinates(x2 + dx, y2 + dy):
                result1.append((x2 + dx, y2 + dy))

            # For part 2:
            x_dec, y_dec = x1 - dx, y1 - dy
            x_inc, y_inc = x2 + dx, y2 + dy

            result2.append((x1, y1))
            result2.append((x2, y2))

            while check_coordinates(x_dec, y_dec):
                result2.append((x_dec, y_dec))
                x_dec -= dx
                y_dec -= dy

            while check_coordinates(x_inc, y_inc):
                result2.append((x_inc, y_inc))
                x_inc += dx
                y_inc += dy
        
            j += 1

print("Part 1 answer: ", len(set(result1)))
print("Part 2 answer: ", len(set(result2)))
