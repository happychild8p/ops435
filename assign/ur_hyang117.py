#!/usr/bin/env python3
import os
import sys
import time
import argparse
'''
   authorship declaration

   __author__: Heedong Yang
   __date__: April 2019
   __version__: 1.0
 
   text to describe the purpose of this script

	OPS435 Assignment 2 - Winter 2019
	Program: ur_hyang117.py
	Author: Heedong Yang
	The python code in this file ur_hyang117.py is original work written by
	Heedong Yang. No code in this file is copied from any other source 
	including any person, textbook, or on-line resource except those provided
	by the course instructor. I have not shared this python file with anyone
	other anything except for submission for grading.  
	I understand that the Academic Honesty Policy will be enforced and violators 
	will be reported and appropriate action will be taken.
'''
def get_login_rec():
	'''
	get_login_rec()
	get_login_rec() will use os.popen() method to read the "last -Fiw" and 
	create file that contains the result of the command, which will be returned
	so that read_login_rec(filelist) can use.

		e.g. get_login_rec() -> login_recs
			 read_login_rec(get_login_rec()) -> read_login_rec(login_recs)
	(END)
	'''
	result = str(os.popen('last -Fiw').read())
	r_list = result.split('\n')

	f = open('lastfile','w')
	for line in r_list[:-3]:
		if line[0:6] == 'reboot':
			pass
		elif "crash" in line or "down" in line or "still logged in" in line:
			pass
		else:
			f.write(line+'\n')
	f.close()
	login_recs = ['lastfile']
	return login_recs
def read_login_rec(filelist): 
	'''
	read_login_rec(filelist)
	read_login_rec(filelist) will takes a list of file(s) which contains user or
	remote host and the login time and lo out time, and will split the context into
	several list which contains userlist, hostlist, login&out time and return 3 lists.
		e.g. 
		<format>

		concat_list => (user shell host login - logout (time))
			L( user1 pts/2 99.88.77.66 Fri Dec 29 18:51:00 2017 - Sat 30 03:25:02 2017 (08:34) )
		ulist => [ user1, user2, user3, ... ]
		hlist => [ 192.168.1.2, 192.168.1.5, 20.30.40.50, ... ]

		e.g. read_login_rec(filelist) -> concat_list, ulist, hlist
			 read_login_rec(get_login_rec()) -> concat_list, ulist, hlist
	(END)
	'''
	context_list = []
	concat_list = []
	users_list = []
	hosts_list = []

	for file in filelist:
		f = open(file, 'r')
		context = f.read()
		context_list = context.split('\n')
		for line in context_list[:-1]:
				concat_list.append(line)
		f.close()
	for line in concat_list:
		user = line.split()[0]
		host = line.split()[2]	
		users_list.append(user)
		hosts_list.append(host)

	ulist = sorted(set(users_list))
	hlist = sorted(set(hosts_list))

	return concat_list, ulist, hlist
def print_list_user(userlist, filelist):
	'''
	print_list_user(userlist, filelist)
	print_list_user(userlist, filelist) will takes two parameters userlist and filelist from read_login_rec()
	and user input file list. and print user in the user list line by line from the filelist
		
		e.g. ulist1 = [ user1, user2, user3, ...]
			 flist1 = [ file1, file2, file3, ...] 
			
			 print_list_user(ulist1, flist1) 
			 --> User list for file1, file2, file3,...
			 --> ==================================
			 --> user1
			 --> user2
			 --> user3
			 --> ...
	(END)
	'''
	line1 = "User list for "+', ' .join(filelist)
	print(line1)
	for i in range(len(line1)):
		print("=", end='')
	print('')
	for user in userlist:
		print(user)
def print_list_host(hostlist, filelist):
	'''
	print_list_host(hostlist, filelist)
	print_list_host(hostlist, filelist) will takes two parameters hostlist and filelist from read_login_rec()
	and user input file list. and print remote host in the host list line by line from the filelist
		
		e.g. hlist1 = [ 192.168.1.2, 192.168.2.3, 99.88.77.66, ...]
			 flist1 = [ file1, file2, file3, ...] 
			
			 print_list_user(ulist1, flist1) 
			 --> User list for file1, file2, file3,...
			 --> ==================================
			 --> 192.168.1.2
			 --> 192.168.2.3
			 --> 99.88.77.66
			 --> ...
	(END)
	'''
	line1 = "Host list for "+', ' .join(filelist)
	print(line1)
	for i in range(len(line1)):
		print("=", end='')
	print('')
	for host in hostlist:
		print(host)	
def cal_daily_usage(subject,login_recs):
	'''
	cal_daily_usage(subject, login_records)
	cal_daily_usage(subject, login_records) will takes twok parameters. Firstly, subject is either username
	or remote host ip address. Second parameter, login_records is the list that contains the log in time
	and log out time(generated from read_login_rec(filelist) function), which will be compared with the 
	first argument subject. This function will then calculate how long given subject has logged in daily 
	and return dictionary which key is the date and value is seconds of logged in time.

		e.g. subject = "user1"
			 list1 = 
		['user1   pts/21   99.247.24.199    Fri Dec 29 18:51:00 2017 - Sat Dec 30 03:25:02 2017  (08:34)'
		, 'user2   pts/0    99.247.24.199    Fri Dec 29 02:30:11 2017 - Fri Dec 29 03:25:04 2017  (00:54)]
			 cal_daily_usage(subject, recordlist) -> dictionary1
			 cal_daily_usage("user1", list1) -> dictionary1 = { 2017 12 29:131233 , 2017 12 30 : 12321 }
	(END)
	'''
	container = [] #list by line
	in_out = [] # etc + logindate '-'<--(devider) logoutdate + etc 
	list_login = [] # contain login date weekday, mon_abbrev, day, year
	list_logout = [] # contain logout date wd, m_ab, day, year
	in_date = '' # comparison check with login/out date
	out_date = '' # comparison check with login/out date
	login_time = {} # Dictionary contains date:seconds

	for line in login_recs:
		if line.split()[0] == subject:
			container.append(line.rstrip())
		elif line.split()[2] == subject:
			container.append(line.rstrip())
	for line in container:
		in_out = line.split('-')
		in_date = time.mktime(time.strptime(in_out[0][-25:-14]+in_out[0][-5:-1], '%a %b %d %Y'))
		out_date = time.mktime(time.strptime(in_out[1][1:12]+in_out[1][-13:-9], '%a %b %d %Y'))

		if in_date == out_date:
			list_login.append(in_out[0][-25:-1])
			list_logout.append(in_out[1][1:25])
		elif in_date != out_date:
			list_login.append(in_out[0][-25:-1])
			list_logout.append(time.ctime(in_date + 86399))
			in_date = in_date + 86400
			while in_date != out_date:
				list_login.append(time.ctime(in_date))
				list_logout.append(time.ctime(in_date + 86399))
				in_date = in_date + 86400
			if in_date == out_date:
				list_login.append(time.ctime(in_date))
				list_logout.append(in_out[1][1:25])
	i = 0
	while i < len(list_login):
		intime = time.strftime("%Y %m %d", time.strptime(list_login[i]))
		lin = time.mktime(time.strptime(list_login[i],'%a %b %d %H:%M:%S %Y'))
		lout = time.mktime(time.strptime(list_logout[i],'%a %b %d %H:%M:%S %Y'))
		in_seconds = int(lout) - int(lin)	
		try:
			login_time[intime] += in_seconds
		except:
			login_time[intime] = in_seconds
		i = i + 1
	
	return login_time
def cal_weekly_usage(subject,login_recs):
	'''
	cal_weekly_usage(subject, login_recs)
	cal_weekly_usage(subject, login_recs) will takes twok parameters. First, subject is either username
	or remote host ip address. Second parameter, login_records is the dictionary from the 
	cal_daily_usage(subject,login_recs) which key and value will be contained separate lists, then this
	function will compare the weeknumber of the given date, store the accumulated logged in second in to the
	dictionary splited by week number. The dictionary will be returned.

		e.g. subject = "user1"
			   list1 = 
		['user1   pts/21   99.247.24.199    Fri Dec 29 18:51:00 2017 - Sat Dec 30 03:25:02 2017  (08:34)'
		, 'user1   pts/0    99.247.24.199    Sat Dec 30 02:30:11 2017 - Sun Dec 31 03:25:04 2017  (00:54)]
			 cal_weekly_usage(subject, recordlist) -> dictionary1
			 cal_weekly_usage(subject, cal_daily_usage(subject, login_recs)) -> dictionary2
			 cal_weekly_usage("user1", list1) -> dictionary1 = { 2017 51 : 13123 , 2017 52 : 4321 }
	(END)
	'''
	login_date = list(login_recs.keys())
	login_seconds = list(login_recs.values())
	login_week = []
	login_weektime = {}
	i = 0
	while i < len(login_date):
		seconds = time.mktime(time.strptime(login_date[i], '%Y %m %d'))
		formatted_sec = time.ctime(seconds)
		weeknumber = time.strftime("%Y %W",time.strptime(formatted_sec))
		login_week.append(weeknumber)
		i = i + 1
	i = 0
	while i < len(login_week):
		try:
			login_weektime[login_week[i]] += login_recs[login_date[i]]
		except:
			login_weektime[login_week[i]] = login_recs[login_date[i]]
		i = i + 1
	return login_weektime
def cal_monthly_usage(subject,login_recs):
	'''
	cal_monthly_usage(subject, login_recs)
	cal_monthly_usage(subject, login_recs) will takes twok parameters. First, subject is either username
	or remote host ip address. Second parameter, login_records is the dictionary from the cal_daily_usage
	(subject,login_recs), which key and value will be contained separate lists, then this function will 
	compare the month of the given date, store the accumulated logged in second in to the dictionary
	splited by month(NOT abbreviated form but 1,2,3,4,5, ... format). The dictionary will be returned.

		e.g. subject = "user1"
			   list1 = 
		['user1   pts/21   99.247.24.199    Fri Dec 29 18:51:00 2017 - Sat Dec 30 03:25:02 2017  (08:34)'
		, 'user1   pts/0    99.247.24.199    Tue Jan 01 22:00:00 2018 - Wed Jan 02 03:25:04 2018  (05:25)]
			 cal_monthly_usage(subject, recordlist) -> dictionary1
			 cal_monthly_usage(subject, cal_daily_usage(subject, login_recs)) -> dictionary2
			 cal_monthly_usage("user1", list1) -> dictionary1 = { 2017 12 : 43126 , 2018 01 : 25964 }
	(END)
	'''
	login_date = list(login_recs.keys())
	login_seconds = list(login_recs.values())
	login_month = []
	login_monthly = {}
	i = 0
	while i < len(login_date):
		seconds = time.mktime(time.strptime(login_date[i], '%Y %m %d'))
		formatted_sec = time.ctime(seconds)
		monthnumber = time.strftime("%Y %m", time.strptime(formatted_sec))
		login_month.append(monthnumber)
		i = i + 1
	i = 0
	while i < len(login_month):
		try:
			login_monthly[login_month[i]] += login_recs[login_date[i]]
		except:
			login_monthly[login_month[i]] = login_recs[login_date[i]]
		i = i + 1
	return login_monthly   
def print_usage(dayweekmon, data, subject):
	'''
	print_usage(dayweekmon, data, subject)
	print_usage(dayweekmon, data, subject) takes three parameters dayweekmon, data, and subject. 
	dayweekmon is used to determine the key word is daily, weekly, or monthly so that write lines will
	be executed. data is the dictionary from cal_daily_usage(), cal_weekly_usage(), or cal_monthly_usage()
	this dictionary will be divided and used to generate formatted output. subject is the username or host.
		
		e.g. login_daily = { 2017 12 29:131233 , 2017 12 30 : 12321 }
			 login_weekly = { 2017 51 : 13123 , 2017 52 : 4321 }
			 login_monthly = { 2017 12 : 43126 , 2018 01 : 25964 } 
		print_usage("Daily", login_daily) 
		-> (Daily/WeeklyMonthly) Usage Report for (user1/99.88.77.66)
		-> ==========================================================
		-> (Date/Week #/Month)          		Usage in Seconds
		-> 2017 12 29/ 2017 51/ 2017 12 			131233/ 13123/ 43126
		-> 2017 12 30/ 2017 52/ 2018 01				12321/ 4321/ 25964
		-> Total									(total_value_of_the_result)
	(END)
	'''
	line1 = str(dayweekmon) +" Usage Report for "+str(subject)
	print(line1)
	for i in range(len(line1)):
		print("=", end='')
	print('')
	if dayweekmon == "Daily":
		print("Date          Usage in Seconds")
		key_list = sorted(data.keys())
		key_list.reverse()
		for i in range(len(key_list)):
			print(str(key_list[i])+"        "+str(data[key_list[i]]))
		print("Total             "+str(sum(data.values())))
	elif dayweekmon == "Weekly":
		print("Week #          Usage in Seconds")
		key_list = sorted(data.keys())
		key_list.reverse()
		for i in range(len(key_list)):
			print(str(key_list[i])+"           "+str(data[key_list[i]]))
		print("Total             "+str(sum(data.values())))
	elif dayweekmon == "Monthly":
		print("Month           Usage in Seconds")
		key_list = sorted(data.keys())
		key_list.reverse()
		for i in range(len(key_list)):
			print(str(key_list[i])+"             "+str(data[key_list[i]]))
		print("Total               "+str(sum(data.values())))
def verbose(file, subject, option, is_user):
	'''
	verbose(file, subject, option, is_user)
	verbose(file, subject, option, is_user) takes 4 parameters first, file list from the user input, second
	subject which can be the user or IP, the option which can be the list, daily, weekly or monthly and is_user
	boolean value to determine subject is user or host IP. Subsequently, this funtion will print out the 
	key words, or datas beform major function will be run.
			
		e.g. args.type can be daily, weekly or monthly.

			 verbose(args.F, args.list, "list", True) 
			 verbose(args.F, args.list, "list", False) 

			 -> Files to be processed: ['file_for_check']
			 ->	Type of args for files <class 'list'>
			 -> processing usage report for the following:
			 -> reading login/logout record files ['file_for_check']
			 -> Generating list for user

			 verbose(args.F, args.HOST, args.type, True) 
			 verbose(args.F, args.RHOST, args.type, False)
			 
			 ->Files to be processed: ['a2_test_data_2']
			 -> Type of args for files <class 'list'> 
			 -> usage report for user: user5
			 -> usage report type: weekly
 			 -> processing usage report for the following:
 			 -> reading login/logout record files ['a2_test_data_2']
	(END)
	'''
	print("Files to be processed:" + str(file))
	print("Type of args for files " + str(type(file)))
	if option == "list":
		print("processing usage report for the following: ")
		print("reading login/logout record files "+ str(file))
		print("Generating list for "+ subject)
	else:
		if is_user == True:
			print("usage report for user: "+str(subject))
		elif is_user == False:
			print("usage report for remote host: "+str(subject))			
		print("usage report type: "+ str(option))
		print("processing usage report for the following: ")
		print("reading login/logout record files "+str(file))

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description ="Usage Report based on the last command", epilog = "Copyright 2019 - Heedong Yang")
	parser.add_argument("F", nargs='+', help= "list of files to be processed")
	parser.add_argument("-l", "--list",choices = ["user", "host"], help ="generate user name or remote host IP from the given files") 
	parser.add_argument("-r", "--rhost", dest = "RHOST", help ="usage report for the given remote host IP")
	parser.add_argument("-t", "--type", choices = ["daily", "weekly", "monthly"], help ="type of report: daily, weekly, and monthly")
	parser.add_argument("-u", "--user", dest = "USER", help ="usage report for the given user name")
	parser.add_argument('-v',"--verbose", action ="store_true", help ="tune on output verbosity")
	args = parser.parse_args()

	if args.F[0] == 'last':
		concat_list, ulist, hlist = read_login_rec(get_login_rec())
	else:
		concat_list, ulist, hlist = read_login_rec(args.F)

	if args.verbose:
		if args.list == 'user':
			verbose(args.F, args.list, "list", True)
		elif args.list == 'host':
			verbose(args.F, args.list, "list", False)
		elif args.type == "daily":
			if args.USER:
				verbose(args.F, args.USER, args.type, True)
			elif args.RHOST:
				verbose(args.F, args.RHOST, args.type, False)
		elif args.type == "weekly":
			if args.USER:
				verbose(args.F, args.USER, args.type, True)
			elif args.RHOST:
				verbose(args.F, args.RHOST, args.type, False)
		elif args.type == "monthly":
			if args.USER:
				verbose(args.F, args.USER, args.type, True)
			elif args.RHOST:
				verbose(args.F, args.RHOST, args.type, False)

	if args.list == 'user':
		print_list_user(ulist, args.F)
	elif args.list == 'host':
		print_list_host(hlist, args.F)

	if args.type == "daily":
		if args.USER:
			login_time = cal_daily_usage(args.USER, concat_list)
			print_usage("Daily", login_time, args.USER)
		elif args.RHOST:
			login_time = cal_daily_usage(args.RHOST, concat_list)
			print_usage("Daily", login_time, args.RHOST)
		
	elif args.type == "weekly":
		if args.USER:
			login_weektime = cal_weekly_usage(args.USER, cal_daily_usage(args.USER, concat_list))
			print_usage("Weekly", login_weektime, args.USER)
		elif args.RHOST:
			login_weektime = cal_weekly_usage(args.RHOST, cal_daily_usage(args.RHOST, concat_list))
			print_usage("Weekly", login_weektime, args.RHOST)

	elif args.type == "monthly":
		if args.USER:
			login_month = cal_monthly_usage(args.USER, cal_daily_usage(args.USER, concat_list))
			print_usage("Monthly", login_month, args.USER)			
		elif args.RHOST:
			login_month = cal_monthly_usage(args.RHOST, cal_daily_usage(args.RHOST, concat_list))
			print_usage("Monthly", login_month, args.RHOST)