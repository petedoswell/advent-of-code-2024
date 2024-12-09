import numpy as np
import logging

# set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='antenna_pt2_debug.log',
    filemode='w'  
)

with open('day8_input.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)
logging.info(f'grid size: \n{grid}')
# define grid parameters, set vars to ref axes
rows, cols = grid.shape
rows -= 1
cols -=1


def antenna_distance(ant_1, ant_2):
    dist = [
        max(ant_1[0], ant_2[0]) - min(ant_1[0], ant_1[0]),
        max(ant_1[1],ant_2[1]) - min(ant_1[1], ant_2[1])
    ]
    logging.info(f'distance = {dist}')
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

def antenna_distance_slope(ant_1, ant_2):
    
    dist = [
        max(ant_1[0], ant_2[0]) - min(ant_1[0], ant_1[0]),
        max(ant_1[1],ant_2[1]) - min(ant_1[1], ant_2[1])
    ]
    logging.info(f'distance = {dist}')
      
    if (max(dist) % min(dist)) > 0:
        return dist
    else: 
        return [int(i/min(dist)) for i in dist]

def vector_dir(antenna_1, antenna_2):
    """ part 2 only """
    y_direction = antenna_1[0] > antenna_2[0]
    x_direction = antenna_1[1] > antenna_2[1]

    if (y_direction and x_direction) or not y_direction and not x_direction:
        logging.info('running y_x_even')
        return y_x_even(antenna_1, dist)
    else:
        logging.info('running y_x_uneven')
        return y_x_uneven(antenna_1, dist)


def y_x_even(antenna, dist):
    """ part 2 only """
    logging.info(f'x_y even antenna: {antenna}')
    antinodes = [antenna]
    positive_antinode = antenna
    negative_antinode = antenna

    for i in range(rows*2):
        positive_antinode = [positive_antinode[0] + dist[0], 
                             positive_antinode[1] + dist[1]]
        antinodes.append(positive_antinode)

    for i in range(rows*2):
        negative_antinode = [negative_antinode[0] - dist[0], 
                             negative_antinode[1] - dist[1]]
        antinodes.append(negative_antinode)
    return(antinodes)


def y_x_uneven(antenna, dist):
    """ part 2 only """
    logging.info(f'x_y uneven antenna: {antenna}')
    antinodes = [antenna]
    positive_antinode = antenna
    negative_antinode = antenna

    for i in range(rows*2):
        positive_antinode = [positive_antinode[0] + dist[0], 
                             positive_antinode[1] - dist[1]] 
        #print(positive_antinode)
        antinodes.append(positive_antinode)
    for i in range(rows*2):
        negative_antinode = [negative_antinode[0] - dist[0], 
                             negative_antinode[1] + dist[1]]
        #print(negative_antinode)
        
        antinodes.append(negative_antinode)
    
    return antinodes


# get list of antenna chars
antennae = np.unique(grid).tolist()
antennae.remove('.')
logging.info(f'\nantennae in grid: {antennae}\n')

antinode_coords = []

for ant in antennae:
    # get indices of element and convert to list
    coords = np.argwhere(grid == ant).tolist()
    logging.info(f'number of {ant} antennae: {len(coords)}')
    logging.info(f'antennae coords: {coords}')

    # compare each antenna to other antennae in list
    for i in range(len(coords)-1):
        antenna_1 = coords.pop(0)
        logging.info(f'antenna 1: {antenna_1}')
        for n in coords:
            antenna_2 = n
            logging.info(f'antenna 2: {antenna_2}')

            #print('ant 1: ',antenna_1,'\nant2: ',antenna_2)

            dist = antenna_distance_slope(antenna_1, antenna_2)
            #print('antenna distance: ', dist)
            #antinode_1, antinode_2 = antinode_position(antenna_1, antenna_2, dist) #part 1 only
            #print('antinode 1: ',antinode_1)
            #print('antinode 2: ',antinode_2)
            antinodes = vector_dir(antenna_1, antenna_2)
            logging.info(f'raw antinodes: {antinodes}')


            for a_node in antinodes:
                # remove out of bounds antinodes
                if (a_node[0] <= rows and a_node[0] >= 0) and (a_node[1] <= cols and a_node[1] >= 0):
                    antinode_coords.append(a_node)

# create list of unique antinodes
unique_antinodes = [list(i) for i in set([tuple(n) for n in antinode_coords])]
logging.info(f'unique_antinodes: {unique_antinodes}')
print(len(unique_antinodes))


"""
issues:

2. incorrect values
    --> try to isolate
"""




   


