# DAY 2

# Preparation

with open('./inputs/day02.txt', 'r') as file:
    input = file.read().split('\n')

processed_input = []
num_of_safe_reports = 0  # for part 1
reports_for_dampener = []  # for part 2

for line in input:
    if not line:
        continue

    processed_input.append([int(x) for x in line.split(' ')])

# FUNCTIONS

def report_safety_test(numlist: list):
    diffs = [(numlist[i] - numlist[i+1]) for i in range(len(numlist) - 1)]

    return(all(0 < diff <= 3 for diff in diffs) or all(-3 <= diff < 0 for diff in diffs))

def problem_dampener_test(numlist: list): 
    for i in range(len(numlist)):
        newlist = [x for index, x in enumerate(numlist) if index != i]
        if report_safety_test(newlist):
            return True
    
    return False

# Part 1

for report in processed_input:
    if report_safety_test(report):
        num_of_safe_reports += 1
    # for part 2:
    else:
        reports_for_dampener.append(report)

print("Safe reports found: ", num_of_safe_reports)

# Part 2

for report in reports_for_dampener:
    if problem_dampener_test(report):
        num_of_safe_reports += 1

print("Safe reports found (with Dampener): ", num_of_safe_reports)