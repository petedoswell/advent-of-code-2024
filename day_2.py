# part 1 

with open('day2_input.txt', 'r') as file:
    data = file.read().splitlines()

# convert each line to list of integers
for line in data:
    data_list = list(map(int, line.split()))






#notes: lines are diff lengths, tf need dynamic (range(len)) process
#TODO: define increasing or decreasing for first 2 numbers (subtraction)
#TODO: iterate through each number in list, determining diff size and increase /decrease consistency
#TODO: incerase counter/bucket list for each line that satisfies conds
    