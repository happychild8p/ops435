#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
	print("Usage: ./lab2d.py name age")
else:
	name = sys.argv[1]
	age = sys.argv[2]
	print("Hi %s, you are %s years old." % (name, str(age)))