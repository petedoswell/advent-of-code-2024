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



def antinode_coords(coords):
    for i in range(len(coords)-1):
        # section off ref antenna
        antenna_1 = coords.pop(0)
        # ref antenna coords
        for a1_x,a1_y in antenna_1:
            # comparison antenna coords
            for a2_x,a2_y in coords:
                # calc dist between ref antenna and comparision antenna
                x_dist = max([a1_x, a2_x]) - min([a1_x], [a2_x])
                y_dist = max([a1_y, a2_y]) - min([a1_y], [a2_y])
                antinode_1 = 


antinode_coords(coords)

def antenna_distance(ant_1, ant_2):
    

#TODO: iterate through group cooords, return antinode coords, save to new list
#TODO: remove out-of-bounds antinode coords.
#TODO: count antinode coords (do overlapping antinodes count as 1 or > 1?)