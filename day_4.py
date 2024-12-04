import numpy as np 

# load data into np array
with open('input_day4.txt', 'r') as file:
    data_list = [list(line) for line in file.read().splitlines()]  
arr = np.array(data_list)

rows, cols = arr.shape

number_xmas = 0

def xmas_counter(slice):
    global number_xmas
    if ''.join(slice) == 'XMAS':
                number_xmas +=1


for x in range(rows):
    for y in range(cols):

        if y + 4 <= cols:
            forward_slice = arr[x, y:(y+4)]
            xmas_counter(forward_slice)
            
        if y - 3 >= 0:
            backward_slice = arr[x,y:(y-4):-1]
            xmas_counter(backward_slice)

        if x + 4 <= rows:
            downward_slice = arr[x:(x+4),y]
            xmas_counter(downward_slice)
        
        if x - 3 >= 0:
            upward_slice = arr[x:(x-4):-1,y]
            xmas_counter(upward_slice)

print(number_xmas)