from typing import Counter

# DAY 1

# Part 1

column1, column2 = [], []
distance = 0

with open('./inputs/0101.txt', 'r') as file:
    input = file.read().split('\n')

for line in input:
    a, b = line.split()
    column1.append(int(a.strip()))
    column2.append(int(b.strip()))

column1.sort()
column2.sort()

for i in range(len(column1)):
    distance += (abs(column1[i] - column2[i]))

print("Distance: ", distance)


# Part 2

column1_occurences = Counter(column1)
column2_occurences = Counter(column2)
similarity_score = 0

for item in column1_occurences.keys():
    print (item, column1_occurences[item], column2_occurences[item])
    similarity_score += int(item) * column1_occurences[item] * column2_occurences[item]

print("Similarity score: ", similarity_score)