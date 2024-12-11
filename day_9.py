import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='defrag_puzzle.log',
    filemode='w'
)

with open('day9_input.txt', 'r') as file:
    data = list(file.read().strip())


# handle odd_numbered input
if len(data)%2 != 0:
    spare = int(data.pop())

# split data into files and free_space
files = [int(data[i]) for i in range(0,len(data),2)]
free_space = [int(data[n]) for n in range(1,len(data),2)]


#create tuples of files and free space
disk_map = list(zip(files, free_space))

# list to store expanded disk map
expanded_disk_map = []

# get ID number of files and free space tuples
for id, value in enumerate(disk_map):

    # expand ID and number of files
    for i in range(value[0]):
        expanded_disk_map.append(id)
    # expand empty space
    for i in range(value[1]):
        expanded_disk_map.append('.')

final_number = [expanded_disk_map[-1] for x in range(spare)]
for z in final_number:
    expanded_disk_map.append(z)

disk_size = len(expanded_disk_map)

for i in range(disk_size):
    if expanded_disk_map[i] == '.':
        expanded_disk_map.reverse()
        for j in range(disk_size):
            if expanded_disk_map[j] != '.':
                holding = expanded_disk_map[j]
                expanded_disk_map[j] = '.'
                expanded_disk_map.reverse()

                break
        expanded_disk_map[i] = holding

for i in range(disk_size):
    if expanded_disk_map[i] == '.':
        holding = expanded_disk_map[-1]
        expanded_disk_map[i] = holding
        expanded_disk_map[-1] = '.'
        break

logging.info(expanded_disk_map)
if len(expanded_disk_map) != len(data):
    logging.debug(f'uneven sizes: \ndiskmap = {len(expanded_disk_map)}\noriginal data = {len(data)}')
checksum = sum([index * value for index, value in enumerate(expanded_disk_map) if value != '.'])
print(checksum)

