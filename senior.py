employee_count = int(raw_input("How many employees are bidding?\n> "))
names = []	#list of each employees name
schedules = []	#list of each available schedule
picks = []	#nested list of each employees choices
final = []	#list of each employee and their awarded schedule

#finds a choice within the nested lists of picks
def find(employee, choice_num):
	nested_list = picks[employee]
	choice = nested_list[choice_num]
	return choice

#adding names and schedule numbers to list
for i in range(1, employee_count + 1):
	names.append(raw_input("Enter employee number %d's name: " % i))
	schedules.append(str(i))

#adding employee picks to list	
for i in range(0, employee_count):
	#converts selections to list with map function
	picks.append(map(str, raw_input("Enter %s's selections in order without any spaces:\n> " % names[i])))
	
#goes through employees 1 by 1 and assigns schedules
for employee in range(0, employee_count):
	choice_num = 0		
	
	while len(final) < employee_count:	
		choice = find(employee, choice_num)

		if choice in schedules:
			#if the employees choice is available this will assign it to them		
			final.append("%s has been awarded schedule number: %s" % (names[employee], choice))
			#deletes choice from schedules list so it cant be assigned again
			schedules.remove(choice)
			#breaks out of the while loop to move on to the next employee
			break	
		
		else:
			#if the employees 1st choice is taken this will add one to 
			#the choice_num variable which will check the availability of their next choice
			choice_num += 1	
			continue
			
print '\n'.join(final)