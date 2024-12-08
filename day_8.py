import numpy as np

with open('day8_example.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)
print(grid)

#TODO: define parameters of grid
#TODO: scrape coords of antenna groups
#TODO: iterate through group cooords, return antinode coords, save to new list
#TODO: remove out-of-bounds antinode coords.
#TODO: count antinode coords (do overlapping antinodes count as 1 or > 1?)