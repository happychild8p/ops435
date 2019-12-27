#!/usr/bin/env python3
'''
OPS435 Assignment 1 - Winter 2019
Program: a1_hyang117.py
Author: Heedong Yang

The python code in this file a1_hyang117.py is original work written by
Heedong Yang. No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and 
violators will be reported and appropriate action will be taken.

'''

import os
import sys

#def usage():
######################################################################
def usage(list1):
	'''
	usage() will take one argument and check if there is --step option is on or not.
	if there is --step option, it will call the step function to work, if not,	
	check the type the type of the variables, if there is an error,
	print Usage examples, if no errors are occured, then,
	return a string describing the usage of the script    

	i.e) usage() 
	Usage: ./a1_hyang117.py [--step] YYYYMMDD +/-n
	Example: ./a1_hyang117.py 20190216 365
	Example2: ./a1_hyang117.py --step 20190216 5
	
	(END)
	'''
	#Check if 3 arguments and one of them is "--step"
	
	if len(list1) == 4 and "--step" in list1:
		location_of_step = list1.index("--step")
		base_date = str(list1[int(location_of_step) + 1])
		days = int(list1[int(location_of_step) + 2])
		step = True
	#Get the user input and put them in the variable

	#Check if 2 arguments are typed
	elif len(list1) != 3:
		print("Usage: ./a1_hyang117.py [--step] YYYYMMDD +/-n")
		print("Example: ./a1_hyang117.py 20190216 365")
		print("Example2: ./a1_hyang117.py --step 20190216 5")
		sys.exit()

	else:
		base_date = str(list1[1])
		days = int(list1[2])
		step = False
	argv_list = [ base_date, days, step]
	return argv_list
#######################################################################
def step(argv_list):
	'''
	step(list_variable) will take one argument which is list checked by usage(list1)
	function which checks if --step has entered.

	Example: import a1_hyang117
	Example: a1_hyang117.step(argument1)
	argument1 => type list
	argument1[0] => base_date
	argument1[1] => calculation 
	
	it will check the argument and argument is greater than 0 will call tomorrow
	and print 1 by 1, else call yesterday and print 1 by 1.
	
	(END)
	'''
	
	i = argv_list[1]
	if i >= 0:
		for i in range(1, i+1):
			print(dbda(argv_list[0], i))
	else:
		listing = []
		for i in range(i, 0):
			listing.append(dbda(argv_list[0], i))
		listing.reverse()
		for item in listing:
			print(item)

#######################################################################
def leap_year(year):
	'''
	leap_year(int_variable)
	It will retrieve the 4 digit integer and determine 29th day of February is exist.
	It will return either 28 or 29
	if year is divisible by 4, 29 will be returned
	if year is divisible by 400, 29 will be returned.
	if year is divisible by 100, 28 will be returned.
	*divisible by 400 would take precedence.
	else 28 will be returned.

	e.g. leap_year(2016) -> 29
		 leap_year(2019) -> 28
		 leap_year(1600) -> 29
		 leap_year(1700) -> 28

	(END)
	'''	
	leap_year = year % 4 #First Rule... 
	if leap_year == 0:
		feb_max = 29
	else:
		feb_max = 28

	leap_year = year % 100 #Second Rule (Mind the order)
	if leap_year == 0:
		feb_max = 28
	leap_year = year % 400
	if leap_year == 0:
		feb_max = 29
	return feb_max
#########################################################################
def tomorrow(today):
	'''
	tomorrow(string_value)
	tomorrow() takes a valid date string in 'YYYYMMDD' format and return a
		date string for the next day in 'YYYYMMDD' format.

		e.g. tomorrow('20171231') -> '20180101'
			 tomorrow('20180131') -> '20180201'
			 tomorrow('20180228') -> '20180301'
	(END)
	'''
	if len(today) != 8:
		return '00000000'
	else:
		#Devide date in to yyyy,mm,dd
		year = int(today[0:4])
		month = int(today[4:6])
		day = int(today[6:])
		tomorrow = day + 1 #Defining tomorrow
		month_max = days_in_mon(leap_year(year))
		
		if tomorrow > month_max[month]: #Add month and make day back to 1
			tomorrow = 1
			month = month + 1
			if month > 12: # Check if month is valid( in range(12))
				month = 1
				year = year + 1

		result = str(year) + str(month).zfill(2) + str(tomorrow).zfill(2)

		return result
##########################################################################	
def yesterday(today):
	'''
	yesterday(string_value)
	yesterday() takes a valid date string in 'YYYYMMDD' format and return a 
		date string for the previous day in 'YYYYMMDD' format.
		
		e.g. yesterday('20181231') -> '20181230'
			 yesterday('20160301') -> '20160229'
			 yesterday('20180101') -> '20171231'
	(END)
	'''
	if len(today) != 8:
		return '00000000'
	else:
		year = int(today[0:4])
		month = int(today[4:6])
		day = int(today[6:])
		yesterday = day - 1 #Defining yesterday
		month_max = days_in_mon(leap_year(year))
		
		if yesterday == 0:
			month = month - 1
			if month not in(month_max.keys()):
				month = 12
				year = year - 1
				yesterday = 31
			else:
				yesterday = month_max[month]

		result = str(year) + str(month).zfill(2) + str(yesterday).zfill(2)
		return result
##########################################################################

def days_in_mon(feb_max): 
	'''
	This function will get the leap_year function's return value and 
	will determine the maximum date of months
	it will also determined feb_max day according to the year 
	decided by leap_year function

	e.g. day_in_mon(29) -> {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
		 day_in_mod(28) -> {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31 } 
	(END)
	'''
	month_max = {1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
	return month_max
##########################################################################
def valid_date(user_input):
	'''
	This funtion will check if the value of the month and day of user input
	if month or date value is out of range, it will halt the script and 
	Print Error message.
	
	e.g. valid_date(sys.argv)
	sys.argv[1] -> month will be checked.
	sys.argv[2] -> day will be checked.

	(END)
	'''
	
	if len(user_input) == 4:
		valid = user_input[2]
	if len(user_input) == 3:
		valid = user_input[1]
	if len(valid) != 8:
		print("Error: wrong date entered")

	year = int(valid[0:4])
	month = int(valid[4:6])
	day = int(valid[6:])

	max_day = days_in_mon(leap_year(year))
	
	if month not in range(1, 13):
		print("Error: wrong month entered")
		sys.exit()
	if day > max_day[month]:
		print("Error: wrong day entered")
		sys.exit()
##########################################################################
def bonus(list1):
	base_date = str(list1[0])
	goal = str(list1[1])
	i = 0
	if base_date >= goal:
		while base_date != goal:
			base_date = tomorrow(base_date)
			i = i + 1
	else:
		while base_date != goal:
			base_date = yesterday(base_date)
			i = i + 1
	return i
		
##########################################################################
def dbda(yyyymmdd, days):
	'''
	dbda function will get yyyymmdd (given date from user_input)
	and get days and check if days is negative # or positive #
	based on +/-, it will call tomorrow or yesterday function wtih
	while loop until range(given_date) iterationwill be finished.

	e.g. dbda(20101010, 10) -> 20101020
		 dbda(20190101, -3) -> 20181229
		 dbda(20160227, 2) -> 20160229

	(END)
	'''

	if days >= 0:#If it is future??
		for one in range(days):
			yyyymmdd = tomorrow(yyyymmdd)

	else:#Or it is past
		for one in range(abs(days)):
			yyyymmdd = yesterday(yyyymmdd)
	return yyyymmdd

##########################################################################
#################           MAIN             #############################
'''
main will basically call 
1. valid_date() -> to check valid(usable) values are entered.
2. check further errors(length of input, --step option) and create list to be used 
	by other functions.
3. if --step is triggered, run step function
4. if --step is not triggered, evoke dbda to be run so it will check the value and
	call tomorrow, or yesterday funtion and iteration.
'''
if __name__ == "__main__":
	
	valid_date(sys.argv)
	argv_list = usage(sys.argv)
#	i = 0
#	if len(argv_list[0]) == 8 and argv_list[1] == 8:
#		bonus(argv_list)
	if argv_list[2] == True and argv_list[1] >= 0:
		step(argv_list)
	elif argv_list[2] == True and argv_list[1] < 0:
		step(argv_list)
#elif len(argv_list[1]) == 8:
#	while argv_list[0] != 
	else:
		print(dbda(argv_list[0], argv_list[1]))

