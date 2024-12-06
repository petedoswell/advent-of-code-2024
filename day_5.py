from collections import defaultdict
import logging

# set up logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='manuals_debug.log',
    filemode='w'  
)

with open('day5_input.txt', 'r') as file:
    data = file.read().splitlines()

# split data into relevant objects
page_order = [tuple(dat.split(r'|')) for dat in data if r'|' in dat]
manuals = [dat.split(',') for dat in data if r'|' not in dat]

# make dict of page orders
print_order = defaultdict(list)
for a, b in page_order:
    print_order[a].append(b)

valid_manuals = []
invalid_manuals = []


def check_all_pages(source_page, checklist):
    """ check source page is out of order """
    for page in checklist:
        check_pages = print_order.get(page)
        try:
            if source_page in check_pages:
                return False
        # handle source page with empty check pages
        except TypeError:
            logging.debug(f'empty list for source page {page}')
            return True
    return True


for manual in manuals:

    invalid_pages = False
    logging.info(f'starting manual{manual}')

    for i in range(len(manual)-1):
        source_page = manual[i]
        check_list = manual[i+1:]
        in_order = check_all_pages(source_page, check_list)

        if not in_order:
            invalid_pages = True
            invalid_manuals.append(manual)
            break
    if invalid_pages:
        continue
    else: 
        valid_manuals.append(manual)
        

print(f'total manuals:{len(manuals)}')
print(f'valid manuals:{len(valid_manuals)}')
print(f'invalid manuals:{len(invalid_manuals)}')
# remove empty list due to blank row in source file
del valid_manuals[0]

middle_pages = []

for v_manual in valid_manuals:
    int_manual = list(map(int, v_manual))
    middle_page = int_manual[len(int_manual)// 2]
    middle_pages.append(middle_page)

print(sum(middle_pages))

