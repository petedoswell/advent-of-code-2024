# part 1 

with open('day2_input.txt', 'r') as file:   
    data_list = [list(map(int, line.split())) for line in file.read().splitlines()]

safe_count = 0
safe_list = []
unsafe_list = []
test_list = []

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
        unsafe_list.append(dat)
        continue
    # fluctuation = unsafe
    if increase and decrease:
        unsafe_list.append(dat)
        continue
    else:
        safe_list.append(dat)
        safe_count += 1

print(f'original safe count: {safe_count}')


# part 2

def direction(reactor):
    # check if all increasing
    increasing = all(reactor[i] < reactor[i + 1] for i in range(len(reactor) - 1))
    # check if all decreasing
    decreasing = all(reactor[i] > reactor[i + 1] for i in range(len(reactor) - 1))

    return increasing or decreasing


def valid_gaps(reactor):
    # check all gaps
    return all(1 <= abs(reactor[i] - reactor[i + 1]) <= 3 for i in range(len(reactor) - 1))


def is_safe(reactor):
    # combine all safety checks
    return direction(reactor) and valid_gaps(reactor)


def safe_if_dampened(reactor):
    for i in range(len(reactor)):

        # simulate reactor w/o unsafe element
        dampened_reactor = reactor[:i] + reactor[i + 1:]  
        # check safety w/o unsafe element
        if is_safe(dampened_reactor):
            return True
        
    return False


def count_safe_reactors(data):
    # runner func
    safe_count = 0
    for reactor in data:
        if is_safe(reactor) or safe_if_dampened(reactor):
            safe_count += 1

    return safe_count


safe_reactors = count_safe_reactors(data_list)
print(f'adjusted safe count: {safe_reactors}')


