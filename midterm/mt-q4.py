#!/usr/bin/python3

def get_mark():
	mark = input("Please enter a mark (0-100): ")
	return int(mark)

def mark_2_grad(mark):
	if mark in range(90, 101):
		grade = "A"
	elif mark in range(80, 90):
		grade = "B"
	elif mark in range(70, 80):
		grade = "C"
	elif mark in range(60, 70):
		grade = "D"
	else:
		grade = "F"
	
	return grade

print("Your grade is "+ mark_2_grad(get_mark()))




