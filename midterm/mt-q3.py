#!/usr/bin/python3

import sys

while True:
    print("Enter any two numbvers:")
    first = int(input("Please enter the first number: "))
    second = int(input("Please enter the second number: "))

    if first % second == 0:
	    print("OK, "+str(second)+ " is divisible by "+str(first)+". Thanks!")
	    sys.exit()
    else:
	    print(str(second)+" is not divisible by "+str(first)+". Please try again.")



