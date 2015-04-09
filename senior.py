from sys import exit

names = []	#list of each employees name
schedules = []	#list of each available schedule
picks = []	#nested list of each employees choices
final = []	#list of each employee and their awarded schedule

def start():
	print "What would you like to do?"
	print "1) Start a new session"
	print "2) View most recent session"
	print "3) Quit"
	
	while True:
		next = raw_input("> ")
		
		if next == "1":
			session(True)
		
		elif next == "2":
			session(False)
		
		elif next == "3":
			exit()
		
		else:
			print "I don't understand. Try typing 1, 2, or 3."
	
#if argument is True then session() starts taking input for a new schedule 
#else if argument is False then session() will display the previous schedule	
def session(new):
	if new == True:
		global employee_count
		employee_count = int(raw_input("How many employees are bidding?\n> "))
		#clearing all lists in case they still hold values
		del names[:]
		del schedules[:]
		del picks[:]
		del final[:]
		
		#adding names and schedule numbers to an empty list
		for i in range(1, employee_count + 1):
			names.append(raw_input("Enter employee number %d's name: " % i))
			schedules.append(str(i))
			
		#adding employee picks to list	
		for i in range(0, employee_count):
			#converts selections to list with map function
			picks.append(map(str, raw_input("Enter %s's top %d selection(s) in order without any spaces:\n> " % (names[i], i + 1))))
			
		print "Would you like to save and assign schedules?"
		print "1) Yes"
		print "2) No"
		
		while True:
			next = raw_input("> ")
			
			if next == "1":
				assign()
			
			elif next == "2":
				start()
				
			else:
				print "I don't understand. Try typing 1 or 2."
	
	#displays previous schedule then returns to start()
	else:
		schedule(False)

#finds a choice within the nested lists of picks
def find(employee, choice_num):
	nested_list = picks[employee]
	choice = nested_list[choice_num]
	return choice	
		
#goes through employees 1 by 1 and assigns schedules
def assign():	
	for employee in range(0, employee_count):
		choice_num = 0		
	
		while True:	
			choice = find(employee, choice_num)

			if choice in schedules:
				#if the employees choice is available this will assign it to them		
				final.append("%s has been awarded schedule number: %s" % (names[employee], choice))
				#deletes choice from schedules list so it cant be assigned again
				schedules.remove(choice)
				#breaks out of the while loop to move on to the next employee
				break

			elif int(choice) not in range(1, len(names) + 1):
				#if a choice is out of range of available schedules an error is raised
				raise Exception("%s's choice of %s is out of the range of available schedules to bid for." % (names[employee], choice))
		
			else:
				#if the employees 1st choice is taken this will add one to 
				#the choice_num variable which will check the availability of their next choice
				choice_num += 1	
				continue
				
	schedule(True)

#if the 'new' argument is True then schedule() will open a txt file and record the schedule	then print it
#if the 'new' argument is False then schedule() will print the last recorded schedule
def schedule(new):
	if new == True:		
		with open('Schedule.txt', 'w') as file:
			file.write('\n'.join(final))
			
		print '\n' + '\n'.join(final) + '\n'
		start()
			
	else:
		#a+ mode is used so if the file doesn't exist is will be created
		with open('Schedule.txt', 'a+') as file:
			print '\n' + file.read() + '\n'
			start()
				
start()