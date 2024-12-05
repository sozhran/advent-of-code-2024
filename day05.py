# DAY 5

# Preparation

from itertools import count

with open('./inputs/day05.txt', 'r') as file:
    input = file.read().split('\n')

empty_line_index = next(i for i, j in zip(count(), input) if j == "")

updates = input[empty_line_index + 1:]

ordering_rules = []

for line in input[:empty_line_index]:
    line = line.split('|')
    ordering_rules.append(line[0] + line[1])

#FUNCTIONS

def sorted_checker(data: list):
    if all(data[i] + data[i+1] in ordering_rules for i in range(len(data) - 1)):
        return True
    
    return False

# Parts 1 & 2

result1 = 0
result2 = 0

for update in updates:
    if not update:
        continue

    update = update.split(',')

    middle_index = (len(update) - 1) // 2

    if sorted_checker(update):
        result1 += int(update[middle_index])
        continue

    sorted = False

    while sorted == False:
        for i in range(len(update) - 1):
            if update[i] + update[i+1] not in ordering_rules:
                update[i], update[i+1] = update[i+1], update[i]
        if sorted_checker(update):
            sorted = True
    
    result2 += int(update[middle_index])

print("Part 1 answer: ", result1)
print("Part 2 answer: ", result2)
