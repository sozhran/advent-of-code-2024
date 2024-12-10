# DAY 6

# Preparation

from itertools import count

with open('./inputs/day06.txt', 'r') as file:
    input = file.read().split('\n')

for line in input:
    if not line:
        input.remove(line)

# Part 1

def change_direction(direction):
    if direction == "up":
        return "right"
    if direction == "right":
        return "down"
    if direction == "down":
        return "left"
    if direction == "left":
        return "up"

def check_next_position(x, y, direction):
    if direction == "up":
        return x, y-1
    if direction == "right":
        return x+1, y
    if direction == "down":
        return x, y+1
    if direction == "left":
        return x-1, y
    
starting_y = next(i for i, line in zip(count(), input) if "^" in line)
starting_x = next(i for i, char in zip(count(), input[starting_y]) if char == "^")

max_x = len(input[0]) - 1
max_y = len(input) - 1

def border_check(x, y):
    if x == 0 or x == max_x or y == 0 or y == max_y:
        return True
    
    return False    

def walk_the_walk():
    visited_positions = []
    direction = "up"
    
    x, y = starting_x, starting_y

    visited_positions.append(str(x) + "_" + str(y))
    
    border_reached = border_check(x, y)

    while border_reached == False:
        next_x, next_y = check_next_position(x, y, direction)

        if input[next_y][next_x] == "#":
            direction = change_direction(direction)
            continue
        
        else:
            x, y = next_x, next_y
            visited_positions.append(str(x) + "_" + str(y))
            border_reached = border_check(x, y)

    return visited_positions

unique_visited_positions = set(walk_the_walk())

print("Part 1 answer: ", len(unique_visited_positions))

# Part 2
# A guard will be considered stuck in a loop if she approaches the same obstacle from the same direction twice.
# To save time, we can only look at the turns and skip the straight paths.

loopable_positions = 0

position_num = 0

for position in unique_visited_positions:
    x, y = starting_x, starting_y
    obstacle_x, obstacle_y = [int(a) for a in position.split("_")]
    direction = "up"

    test_input = [row for row in input]
    test_input[obstacle_y] = test_input[obstacle_y][:obstacle_x] + "#" + test_input[obstacle_y][obstacle_x+1:]

    border_reached = border_check(x, y)

    path = []

    while border_reached == False:
        next_x, next_y = check_next_position(x, y, direction)

        if test_input[next_y][next_x] != "#":
            x, y = next_x, next_y
            border_reached = border_check(x, y)

        else:
            next_turn = str(next_x) + "_" + str(next_y) + "_" + direction
        
            if next_turn in path:
                loopable_positions += 1
                break
            else:
                path.append(next_turn)
                direction = change_direction(direction)

print("Part 2 answer: ", loopable_positions)
