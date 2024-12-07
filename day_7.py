import binarytree

with open('day7_example.txt', 'r') as file:
	data = [line.split() for line in file.read().splitlines()]
	
for dat in data:
	dat[0] = dat[0].replace(r':', '') 
	
data = [list(map(int, dat)) for dat in data]

valid_list = []

for dat in data:
    print('dat:' , dat)
    ref_number = dat[0]
    print('ref_number: ', ref_number)
    
    # insert top level for loop
    previous_level = [dat[1]]
    print('previous level: ', previous_level)

    for i in range(2, len(dat)):

        new_level_addition = [dat[i] + p for p in previous_level]
        new_level_multiplication = [dat[i] * p for p in previous_level]

        new_level = zip(new_level_addition, new_level_multiplication)
        flatten_new_level = [num for tp in new_level for num in tp ]
        print('flattened list: ', flatten_new_level)

        previous_level = flatten_new_level

    if ref_number in previous_level:
        valid_list.append(ref_number)

print(valid_list)