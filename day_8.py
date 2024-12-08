import numpy as np

with open('day8_example.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)

# define grid parameters, set vars to ref axes
rows, cols = grid.shape

# get list of antenna chars
antennae = np.unique(grid).tolist()
antennae.remove('.')
print(f'\nantennae in grid: {antennae}\n')

for ant in antennae:
    # get indices of element and convert to list
    coords = np.argwhere(grid == ant).tolist()
    print(f'{ant} coords: {coords}')


#TODO: iterate through group cooords, return antinode coords, save to new list
#TODO: remove out-of-bounds antinode coords.
#TODO: count antinode coords (do overlapping antinodes count as 1 or > 1?)