from collections import defaultdict

with open('day_5_example.txt', 'r') as file:
    data = file.read().splitlines()

page_order = [tuple(dat.split(r'|')) for dat in data if r'|' in dat]
manuals = [dat.split(',') for dat in data if r'|' not in dat]

print_order = defaultdict(list)
for a, b in page_order:
    print_order[a].append(b)

valid_manuals = []
invalid_manuals = []

for manual in manuals:
    print(f'starting manual{manual}')
    for i in range(len(manual)-1):
        print(f'source page: {manual[i]}')
        print(f'check pages: {manual[i+1:]}')
        print(f'dictionary contents: {print_order[manual[i]]}')

        check = all(pg in print_order[manual[i]] for pg in manual[i+1:])
        if not check:
            invalid_manuals.append(manual)
            break



print(f'total manuals:{len(manuals)}')
print(f'valid manuals:{len(valid_manuals)}')
print(f'invalid manuals:{len(invalid_manuals)}')


    
        

"""
"""  

"""
#TODO: iterate through data(2) using enumerate 
#TODO: check dict v position < | > dict k position 
#TODO: move data(2) list to valid | invalid list
#TODO: get middle number from each valid list (enumerate modulo?)
#TODO: sum middle numbers
"""
