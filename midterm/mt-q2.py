#!/usr/bin/python3

import sys

list1 = sys.argv[1:]
list1.reverse()

for i in range(len(list1)):
	print(list1[i])

print("List provided: "+ str(list1))

