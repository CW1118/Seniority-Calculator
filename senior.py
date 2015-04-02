employee_count = int(raw_input("How many employees are bidding?\n>"))
names = []

for i in range(1, employee_count + 1):
	name = raw_input("Enter employee number %d's name:" % i)
	names.append(name)