import re

#TODO: read file as continuous line
with open('input 2.txt', 'r') as file:
	data = file.read()

#TODO: regex match mul(\d+,\d+) to list
pattern = r'mul\(\d+[,]\d+\)'
matches = re.findall(pattern, data)

#TODO: remove mul 
trimmed = [match.replace('mul', '') for match in matches]
print(trimmed)

#TODO: convert string to numerical tuples

#TODO: multiply tuples
#TODO: sum results

