import numpy as np 

# load data into np array
with open('input_day4.txt', 'r') as file:
    data_list = [list(line) for line in file.read().splitlines()]  
arr = np.array(data_list)

rows, cols = arr.shape

for x in range(rows):
    for y in range(cols):
        forward_slice = arr[x, y:]

        print(forward_slice)