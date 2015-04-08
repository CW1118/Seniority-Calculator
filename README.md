# Seniority-Calculator
A command line script used assign days off to employees based on seniority.

At my current job, every 3 months all the employees bid for new hours and days off based on seniority.  Everyone is
given a list of schedules to choose from for the next quarter.  Each line number is a different schedule(hours/days off)
and everyone writes out a numbered list starting with their most prefered schedule and ending with their least prefered.

Example:
Schedule #            Preference

1(Mon/Tue off)        3

2(Tue/Wed off)        4

3(Sat/Sun off)        1(Most Prefered)

4(Sun/Mon off)        2

5(Wed/Thur off)       5(Least Prefered)

So the #1 person in seniority always gets their 1st choice then everyone afterward only gets their most prefered choice
if it hasn't already been taken by someone higher in seniority than them.  If their 1st choice has already been taken
then you move on to their 2nd most prefered choice and so on.

It's a very time consuming process seeing as it's all done on paper.  So I'm working on an easier and faster method using 
Python.  This is a very beginner friendly project so anyone is welcome to contribute.

If you have any questions email me at: 1118cw@gmail.com
