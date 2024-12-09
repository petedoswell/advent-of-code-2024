with open('day9_example.txt', 'r') as file:
    data = list(file.read())

# split data into files and free_space
files = [int(data[i]) for i in range(0,len(data),2)]
free_space = [int(data[n]) for n in range(1,len(data),2)]

#create tuples of files and free space
disk_map = list(zip(files, free_space))

expanded_disk_map = []

# get ID number of files and free space tuples
for id, value in enumerate(disk_map):
    print(id, value)

