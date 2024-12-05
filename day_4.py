import numpy as np
import logging

# set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='debug.log',
    filemode='w'  
)

# load data into numpy array
with open('input_day4.txt', 'r') as file:
    data_list = [list(line) for line in file.read().splitlines()]
arr = np.array(data_list)

# part 1 

rows, cols = arr.shape
number_xmas = 0

# track matches 
direction_counts = {
    "horizontal_forward": 0,
    "horizontal_backward": 0,
    "vertical_downward": 0,
    "vertical_upward": 0,
    "diagonal_forward_down": 0,
    "diagonal_backward_down": 0,
    "diagonal_forward_up": 0,
    "diagonal_backward_up": 0,
}

# log slice and count matches
def xmas_counter(slice, start, end, category):

    global number_xmas
    slice_content = ''.join(slice)
    if slice_content == 'XMAS':
        number_xmas += 1
        direction_counts[category] += 1
        logging.info(f"Match found in {category} from {start} to {end}: {slice_content}")
    else:
        logging.debug(f"No match in {category} from {start} to {end}: {slice_content}")


# make sure all grid locations are checked
locations_checked = set()


for x in range(rows):
    for y in range(cols):

        # forward slice
        if y + 4 <= cols:
            forward_slice = arr[x, y:(y+4)]
            xmas_counter(forward_slice, start=(x, y), end=(x, y+3), category="horizontal_forward")
            locations_checked.update([(x, yy) for yy in range(y, y+4)])

        # backward explicit slice
        if y - 3 >= 0:
       
            backward_slice = [arr[x, y], arr[x, y-1], arr[x, y-2], arr[x, y-3]]
            logging.debug(f"Horizontal Backward from ({x}, {y}) to ({x}, {y-3}): {''.join(backward_slice)}")
            xmas_counter(backward_slice, start=(x, y), end=(x, y-3), category="horizontal_backward")


        # downward slice
        if x + 4 <= rows:
            downward_slice = arr[x:(x+4), y]
            xmas_counter(downward_slice, start=(x, y), end=(x+3, y), category="vertical_downward")
            locations_checked.update([(xx, y) for xx in range(x, x+4)])

        # upward explicit
        if x - 3 >= 0:
            upward_slice = [arr[x, y], arr[x-1, y], arr[x-2, y], arr[x-3, y]]  # Explicitly construct the slice
            logging.debug(f"Vertical Upward from ({x}, {y}) to ({x-3}, {y}): {''.join(upward_slice)}")
            xmas_counter(upward_slice, start=(x, y), end=(x-3, y), category="vertical_upward")


        # diagonal forward down
        if x + 4 <= rows and y + 4 <= cols:
            diagonal_forward_down = [arr[x+i, y+i] for i in range(4)]
            xmas_counter(diagonal_forward_down, start=(x, y), end=(x+3, y+3), category="diagonal_forward_down")
            locations_checked.update([(x+i, y+i) for i in range(4)])

        # diagonal backward down
        if x + 4 <= rows and y - 3 >= 0:
            diagonal_backward_down = [arr[x+i, y-i] for i in range(4)]
            xmas_counter(diagonal_backward_down, start=(x, y), end=(x+3, y-3), category="diagonal_backward_down")
            locations_checked.update([(x+i, y-i) for i in range(4)])

        # diagonal forward up
        if x - 3 >= 0 and y + 4 <= cols:
            diagonal_forward_up = [arr[x-i, y+i] for i in range(4)]
            xmas_counter(diagonal_forward_up, start=(x, y), end=(x-3, y+3), category="diagonal_forward_up")
            locations_checked.update([(x-i, y+i) for i in range(4)])

        # diagonal backward up
        if x - 3 >= 0 and y - 3 >= 0:
            diagonal_backward_up = [arr[x-i, y-i] for i in range(4)]
            xmas_counter(diagonal_backward_up, start=(x, y), end=(x-3, y-3), category="diagonal_backward_up")
            locations_checked.update([(x-i, y-i) for i in range(4)])

# check all locations used
all_locations = {(x, y) for x in range(rows) for y in range(cols)}
missed_locations = all_locations - locations_checked


print("Total XMAS count:", number_xmas)
print("Matches by direction:", direction_counts)
print("Total locations checked:", len(locations_checked))
print("Missed locations:", missed_locations)

# part 2

number_cross_mas = 0

def mas_check(slice):
    slice_content = ''.join(slice)
    return slice_content in ['MAS', 'SAM']


for x in range(rows - 2): 
    for y in range(1, cols - 1):  

       
        diagonal_forward_down = [arr[x+i, y-1+i] for i in range(3)]
 
        diagonal_backward_down = [arr[x+i, y+1-i] for i in range(3)]


        if mas_check(diagonal_forward_down) and mas_check(diagonal_backward_down):
            number_cross_mas += 1

print(number_cross_mas)


