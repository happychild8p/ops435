#!/usr/bin/env python3

import sys

first = sys.argv[1]
second = sys.argv[2]

if int(first) <= 0:
	print("ValueError: the first argument must be greater than 0.")

else:
	i = 1
	third = ""
	while int(i) <= int(first):
		third = third + second
		i = i + 1

	print(third)
