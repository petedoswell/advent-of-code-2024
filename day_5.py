with open('day5_input.txt', 'r') as file:
    data = file.read().splitlines()

pg_order = [tuple(dat.split(r'|')) for dat in data if r'|' in dat]
prnt_pgs = [dat for dat in data if r'|' not in dat]


#TODO: iterate through data(2) using enumerate 
#TODO: check dict v position < | > dict k position 
#TODO: move data(2) list to valid | invalid list
#TODO: get middle number from each valid list (enumerate modulo?)
#TODO: sum middle numbers

