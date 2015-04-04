employee_count = int(raw_input("How many employees are bidding?\n>"))
names = []
schedules = []
picks = []
final = []

#finds a value within the nested lists of picks
def find(a, b):		#a is employee's list of choices and b is their choice
	nested_list = picks[a]
	item = nested_list[b]
	return item

#adding names and schedule numbers to list
for i in range(1, employee_count + 1):
	names.append(raw_input("Enter employee number %d's name: " % i))
	schedules.append(str(i))

#adding employee picks to list	
for i in range(0, employee_count):
	#converts selections to list with map function
	picks.append(map(str, raw_input("Enter %s's selections in order without any spaces:\n>" % names[i])))
	
#goes through employees 1 by 1 and assigns schedules
for i in range(0, employee_count):

	counter = 0		
	
	while len(final) < employee_count:
	
		item = find(i, counter)

		if item in schedules:
			#if the employees choice is available this will assign it to them		
			final.append("%s has been awarded schedule number: %s" % (names[i], item))
			schedules.remove(item)		#deletes choice from schedules list so it cant be picked again
			break	#breaks out of the while loop to move on to the next employee
		
		else:
			#if the employees 1st choice is taken this will add one to 
			#the counter which will check the availability of their next choice
			counter += 1	
			continue
			
print final


