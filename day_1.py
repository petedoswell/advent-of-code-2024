# part 1

with open('input.txt', 'r') as file:
	data = file.read().splitlines()

list1 = []
list2 = []

for dat in data:
	splitdat = dat.split()
	list1.append(int(splitdat[0]))
	list2.append(int(splitdat[1]))

list1.sort()
list2.sort()

diffs = [abs(a - b) for a, b in zip(list1, list2)]

print(sum(diffs))

# part 2

n = [list2.count(i) for i in list1]
n_multiplication = [(l * n) for l,n in zip(list1, n)]

print(sum(n_multiplication))
