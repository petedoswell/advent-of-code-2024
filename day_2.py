# part 1 

with open('day2_input.txt', 'r') as file:
    data = file.read().splitlines()

# convert each line to list of integers
data_list = [list(map(int, line.split())) for line in data]

safe_count = 0

for dat in data_list:
    l = len(dat) - 1
    increase = False
    decrease = False
    safety = True

    for n in dat:
        # gap too large or no increase/decrease = unsafe
        if abs(n - (n+1)) > 3 or n - (n+1) == 0:
            safety = False
            break
        # increasing
        elif n - (n+1) > 0:
            increase = True
        # decreasing
        elif n - (n+1) < 0:
            decrease = True

    # fluctuation = unsafe
    if not safety: 
        continue
    if increase and decrease:
        continue
    else:
        safe_count += 1

print(safe_count)
        
    




#notes: lines are diff lengths, tf need dynamic (range(len)) process
# note 2: sometimes consecutive numbers don't ascend or descend. So may need to create initial flag, and then check agains this as nunmbers are iterated over
#TODO: define increasing or decreasing for first 2 numbers (subtraction)
#TODO: iterate through each number in list, determining diff size and increase /decrease consistency
#TODO: incerase counter/bucket list for each line that satisfies conds
    