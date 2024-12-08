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


def antenna_distance(ant_1, ant_2):
    dist = [
        max(ant_1[0], ant_2[0]) - min(ant_1[0], ant_1[0]),
        max(ant_1[1],ant_2[1]) - min(ant_1[1], ant_2[1])
    ]
    return dist    


def antinode_position(antenna_1, antenna_2, dist):
    antinode_1 = []
    antinode_2 = []

    if antenna_1[0] > antenna_2[0]:
        antinode_1.append(antenna_1[0] + dist[0])
        antinode_2.append(antenna_2[0] - dist[0])
    else:
        antinode_1.append(antenna_1[0] - dist[0])
        antinode_2.append(antenna_2[0] + dist[0])
    
    if antenna_1[1] > antenna_2[1]:
        antinode_1.append(antenna_1[1] + dist[1])
        antinode_2.append(antenna_2[1] - dist[1])
    else:
        antinode_1.append(antenna_1[1] - dist[1])
        antinode_2.append(antenna_2[1] + dist[1])
    
    return antinode_1, antinode_2




#TODO: iterate through group cooords, return antinode coords, save to new list
#TODO: remove out-of-bounds antinode coords.
#TODO: count antinode coords (do overlapping antinodes count as 1 or > 1?)