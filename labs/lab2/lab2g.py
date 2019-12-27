#!/usr/bin/env python3

import sys

if len(sys.argv) == 2:
	number = int(sys.argv[1])

else:
	number = 3

while number > 0:
	print(number)
	number-=1

print("blast off!")


