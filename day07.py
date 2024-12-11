## DAY 7

## Preparation

from itertools import product

with open('./inputs/day07.txt', 'r') as file:
    input = file.read().split('\n')

## FUNCTIONS

def join_lists(list1: list, list2: list):
    united_list = []

    for i in range(len(list1) -1):
        united_list.append(list1[i])
        united_list.append(list2[i])
    
    united_list.append(list1[-1])
    
    return united_list

def eval_list(list: list):
    sum = list[0]

    for i in range(1, (len(list) -1), 2):
            if list[i] == "+":
                sum += list[i+1]
            if list[i] == "*":
                sum *= list[i+1]
            if list[i] == "c":
                sum = int(str(sum) + str(list[i+1]))
    
    return sum

## Parts 1 & 2

result1 = 0
result2 = 0

for line in input:
    if not line:
        continue

    fits_first_calibration = False

    raw_data = line.split(": ")

    goal_sum = int(raw_data[0])
    numbers = [int(x) for x in raw_data[1].split(' ')]

    operators1 = list(product('+*', repeat=(len(numbers) - 1)))
    operators2 = [x for x in list(product('+*c', repeat=(len(numbers) - 1))) if 'c' in x]

    for combination in operators1:
        united_list = join_lists(numbers, combination)

        if eval_list(united_list) == goal_sum:
            result1 += goal_sum
            fits_first_calibration = True
            break
    
    if fits_first_calibration:
        continue

    for combination in operators2:
        united_list2 = join_lists(numbers, combination)

        if eval_list(united_list2) == goal_sum:
            result2 += goal_sum
            break

print("Part 1 answer: ", result1)
print("Part 2 answer: ", result1 + result2)
