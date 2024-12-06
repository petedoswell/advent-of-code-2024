import numpy as np 

with open('day6_input.txt', 'r') as file:
    data = [list(line) for line in file.read().splitlines()]

grid = np.array(data)


""" 
^ = up
< = left
> = right
v = down
# = obstacle
. = clear path
X = patrol route


to determine: 
- position of guard
- guard direction (i.e. symbol)
- path clear or obstacle

to make:
turning algorithm
moving algorithm

if . or X then move 
if # then turn right
"""
grid = 1
guard_coords = (0,0)
guard_dir = ''

def guard_move(guard_dir, x,y):
    """ define next step for guard """
    if guard_dir == '^':
        step = (x, y+1)
    elif guard_dir == 'v':
        step = (x+1, y)
    elif guard_dir == '<':
        step = (y-1)
    elif guard_dir == '>':
        step = (x, y+1)
    return step

def check_path(x,y):
    """ checks next step for obstacles """
    if (x,y) == '.' or (x,y) == 'X':
        return 'move'
    elif (x,y) == '#':
        return 'turn right'

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

if check_path == 'move':
    #grid(guard_coords) = 'X'
    #grid(guard_coords = guard_dir
    pass
         
elif check_path == 'turn right':
    guard_turn(guard_dir)
    guard_move()