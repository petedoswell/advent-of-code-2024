import numpy as np

with open('day8_input.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)
#print(grid)
# define grid parameters, set vars to ref axes
rows, cols = grid.shape
rows -= 1
cols -=1
print(f'grid size: {rows} x {cols}')

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

# get list of antenna chars
antennae = np.unique(grid).tolist()
antennae.remove('.')
print(f'\nantennae in grid: {antennae}\n')

antinode_coords =[]

for ant in antennae:
    # get indices of element and convert to list
    coords = np.argwhere(grid == ant).tolist()
    #print(f'{ant} coords: {coords}')

    for i in range(len(coords)-1):
        antenna_1 = coords.pop(0)
        for n in coords:
            antenna_2 = n
            #print('ant 1: ',antenna_1,'\nant2: ',antenna_2)

            dist = antenna_distance(antenna_1, antenna_2)
            #print('antenna distance: ', dist)
            antinode_1, antinode_2 = antinode_position(antenna_1, antenna_2, dist)
            #print('antinode 1: ',antinode_1)
            #print('antinode 2: ',antinode_2)

            for a_node in antinode_1, antinode_2:
                if (a_node[0] <= rows and a_node[0] >= 0) and (a_node[1] <= cols and a_node[1] >= 0):
                    antinode_coords.append(a_node)

unique_antinodes = [list(i) for i in set([tuple(n) for n in antinode_coords])]
print(len(unique_antinodes))

