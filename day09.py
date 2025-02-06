# DAY 9

# Preparation

from itertools import batched

with open('./inputs/day09.txt', 'r') as file:
    input = file.read().split('\n')[0]

# Part 1

result1 = 0

# add an empty gap in the end
if len(input) % 2 == 1:
    input += "0"

paired_input = [(int(a), int(b)) for (a, b) in batched(input, 2)]

data = {}
max_index = 0

for id, (file, gap) in enumerate(paired_input):
    for i in range(max_index, max_index + int(file)):
        data[i] = id
    
    max_index += int(file) + int(gap)

downreader = max_index

for upreader in range(len(data)):
    if upreader >= downreader:
        break

    if upreader in data:
        result1 += upreader * data[upreader]
        continue

    while downreader not in data:
        downreader -= 1

    data[upreader] = data[downreader]
    del data[downreader]

    result1 += upreader * data[upreader]

print("Part 1 answer: ", result1)
