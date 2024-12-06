


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

outputs Xs

if . or X move up 
if # then turn right

eg guard coords = (x,y)
guard_dir = <symbol>

def guard_move(guard_dir):

    if guard dir == '^':
        step = (x, y+1)
    elif guard_dir == 'v':
        step = (x+1, y)
    elif guard_dir = '<':
        step = (y-1)
    elif guard_dir == '>':
        step = (x, y+1)
    return step

"""
