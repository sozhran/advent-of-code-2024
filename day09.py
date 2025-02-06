# DAY 9

# Preparation

from itertools import batched, chain

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

# Part 2

result2 = 0
data = []

for id, (file, gap) in enumerate(paired_input):
    data.append({ 'type': 'file', 'size': file, 'id': id })
    data.append({ 'type': 'gap', 'size': gap, 'id': 0 })

for pointer in range(len(data) - 1, 0, -1):
    if data[pointer]['type'] != 'file':
        continue

    try:
        writer_index, writer = next((index, x) for index, x in enumerate(data[:pointer]) if x['type'] == 'gap' and x['size'] >= data[pointer]['size'])
    except StopIteration:
        continue

    data[pointer]['type'] = 'gap'
    data[writer_index]['size'] -= data[pointer]['size']

    data.insert(writer_index, { 'type': 'file', 'size': data[pointer]['size'], 'id': data[pointer]['id']})

id_index = 0

for item in data:
    if item['type'] == 'gap':
        id_index += item['size']
        continue

    for i in range(item['size']):
        result2 += id_index * item['id']
        id_index += 1

print("Part 2 answer: ", result2)
