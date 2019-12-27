#!/usr/bin/env python3

import sys

def quiz(file1):
	f = open(file1, 'r')
	f.seek(0)
	list2 = f.readlines()
	i = 0
	for line in list2:
		if line != '\n':
			print(str(line),end='')
			i = i + 1
		elif line == '':
			continue
	f.seek(0)
	print("Total number of non-blank lines in file: "+str(i))
	f.close()
		
if __name__ == "__main__":
	try:
		quiz(sys.argv[1])
	except FileNotFoundError:
		print("File Error: File "+sys.argv[1]+ " does not exist.")
	except PermissionError:
		print("File Error: Do not have permission to read "+sys.argv[1])
