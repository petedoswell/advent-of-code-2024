import numpy as np 

# load data into np array
with open('input_day4.txt', 'r') as file:
    data_list = [list(line) for line in file.read().splitlines()]  
xmas_array = np.array(data_list)
