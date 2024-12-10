with open('day9_example.txt', 'r') as file:
    data = list(file.read())

# split data into files and free_space
files = [int(data[i]) for i in range(0,len(data),2)]
free_space = [int(data[n]) for n in range(1,len(data),2)]

#create tuples of files and free space
disk_map = list(zip(files, free_space))

# list to store expanded disk map
expanded_disk_map = []

# get ID number of files and free space tuples
for id, value in enumerate(disk_map):
    print(id, value)
    # expand ID and number of files
    for i in range(value[0]):
        expanded_disk_map.append(id)
    # expand empty space
    for i in range(value[1]):
        expanded_disk_map.append('.')

print(expanded_disk_map)

# reversed copy of disk_map to pull files from
rev_disk_map = expanded_disk_map.copy()
rev_disk_map.reverse()

print(rev_disk_map)

# iterate over expanded_disk_map, replpacing '.'s with files from end of rev_copy
for i in range(len(expanded_disk_map)):
	if expanded_disk_map[i] == '.':
		for n in range(len(rev_disk_map)):
			if rev_disk_map[n] != '.':
				expanded_disk_map[i] = rev_disk_map[n]
                # replace moved file with '.' so is skipped in next iteration
				rev_disk_map[n] = '.'
				break

print(expanded_disk_map)

#TODO: need to remove the moved files from end of expanded_disk_map to avoid dupes
#TODO: do I need a 3rd list to assemble the defragged disk_map to avoid indexing errors & dupes?