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

    for n in range(len(dat)-1):
        # gap too large or no increase/decrease = unsafe
        if abs(dat[n] - dat[n+1]) > 3 or (dat[n] - (dat[n+1])) == 0:
            safety = False
            break
        # increasing
        elif (dat[n] - dat[n+1]) > 0:
            increase = True
        # decreasing
        elif (dat[n] - dat[n+1]) < 0:
            decrease = True

    if not safety: 
        continue
    # fluctuation = unsafe
    if increase and decrease:
        continue
    else:
        safe_count += 1

print(safe_count)
        
    



    