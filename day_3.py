import re



#read file as continuous line
with open('input-2.txt', 'r') as file:
	data = file.read()
     
data = 'do()' + data

# part 1

def sum_mul(s):
    #regex match mul(\d+,\d+) to list
    pattern = r'mul\(\d+[,]\d+\)'
    matches = re.findall(pattern, s)

    #convert string to numerical tuples
    trimmed = [tuple(map(int, match.strip('mul()').split(','))) for match in matches]

    #multiply tuples & sum results
    mul = [a*b for a,b in trimmed]

    return(sum(mul))


# part 2

def do_dont(data):
    
    pattern = r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))'
    matches = re.findall(pattern, data)
    
    enabled = True  
    total_sum = 0
    
    for match in matches:
        if match == 'do()':
            enabled = True  
        elif match == "don't()":
            enabled = False  
        elif match.startswith('mul') and enabled:
            nums = tuple(map(int, match.strip('mul()').split(',')))
            total_sum += nums[0] * nums[1]
    
    return total_sum

print(do_dont(data))






