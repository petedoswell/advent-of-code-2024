import numpy as np

with open('day8_example.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)
print(grid)