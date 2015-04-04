employee_count = int(raw_input("How many employees are bidding?\n>"))
names = []
schedules = []
picks = []
final = []

#adding names and schedule numbers to list

for i in range(1, employee_count + 1):
	names.append(raw_input("Enter employee number %d's name:" % i))
	schedules.append(i)

#adding employee picks to list
	
for i in range(0, employee_count):
	picks.append(map(str, raw_input("Enter %s's selections in order without any spaces:\n>" % names[i]))) #converts selections to list with map function
	
