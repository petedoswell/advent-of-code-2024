import numpy as np 

with open('day6_example.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)
print(grid)


guard_coords = (0,0)
guard_dir = ''


def slice(guard_dir,guard_coords):
    """ returns np slice from guard to edge of array """
    if guard_dir == '^':
        upward_slice = grid[guard_coords[0]::-1,guard_coords[1]]
        return  upward_slice
    elif guard_dir == '>':
        right_slice = grid[guard_coords[0],guard_coords[1]:]
        return right_slice
    elif guard_dir == 'v':
        down_slice = grid[guard_coords[0]:,guard_coords[1]]
        return down_slice
    elif guard_dir == '<':
        left_slice = grid[guard_coords[0],guard_coords[1]::-1]
        return left_slice


def guard_turn(guard_dir):
    """ turns guard right """
    if guard_dir == '^':
        return  '>'
    elif guard_dir == '>':
        return 'v'
    elif guard_dir == 'v':
        return '<'
    elif guard_dir == '<':
        return '^'


