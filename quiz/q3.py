#!/usr/bin/env python3

import sys
string = sys.argv[1]

if len(string) == 9:
	odd = ''
	for char in string:
		if  string.index(char) % 2 == 0:
			odd = odd + char

	i = len(odd)
	reverse = ''
	while i >= 1:
		i = i - 1
		reverse = reverse + odd[i]

	print("Thank you for your cooperation.")
	print("Here is the enter code: "+odd)
	print("And the exit code is: "+str(reverse))

elif len(string) == 1:
	print("Sorry, "+string+" has only 1 letter.\nPlease give me a nine-letter word.")
	
else:
	print("Sorry, "+string+" has only "+str(len(string))+ " letters.\nPlease give me a nine-letter word.")


