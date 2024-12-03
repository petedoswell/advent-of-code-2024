import re

# part 1

#read file as continuous line
with open('input-2.txt', 'r') as file:
	data = file.read()

#regex match mul(\d+,\d+) to list
pattern = r'mul\(\d+[,]\d+\)'
matches = re.findall(pattern, data)

#remove mul 
trimmed = [match.replace('mul', '') for match in matches]

#convert string to numerical tuples
trimmed = [tuple(map(int, trim.strip('()').split(','))) for trim in trimmed]

#multiply tuples & sum results
mul = [a*b for a,b in trimmed]
print(sum(mul))
	




