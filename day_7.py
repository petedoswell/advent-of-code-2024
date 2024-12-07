import logging

# set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='optree_debug.log',
    filemode='w'  
)

with open('day7_input.txt', 'r') as file:
	data = [line.split() for line in file.read().splitlines()]
	
for dat in data:
	dat[0] = dat[0].replace(r':', '') 
	
data = [list(map(int, dat)) for dat in data]

valid_list = []

for dat in data:
    ref_number = dat[0]
    logging.info(f'ref number: {ref_number}')
    logging.info(f'parameter numbers: {dat[1:]}')
    
    # insert top level for loop
    previous_level = [dat[1]]

    for i in range(2, len(dat)):

        new_level_addition = [dat[i] + p for p in previous_level]
        logging.info(f'addition list: {new_level_addition}')
        new_level_multiplication = [dat[i] * p for p in previous_level]
        logging.info(f'multiplication list: {new_level_multiplication}')
        new_level_concat = [int((str(p)) + str(dat[i])) for p in previous_level]
        logging.info(f'concat list: {new_level_concat}')

        new_level = zip(new_level_addition, new_level_multiplication, new_level_concat)
        flatten_new_level = [num for tp in new_level for num in tp ]
        logging.info(f'flattened list: {flatten_new_level}')
        

        previous_level = flatten_new_level

    if ref_number in previous_level:
        valid_list.append(ref_number)

print(sum(valid_list))