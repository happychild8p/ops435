#!/usr/bin/python3

import sys

num1 = int(sys.argv[1]) 
num2 = int(sys.argv[2])
result = num1 * num2

guess = input("Please enter how much is "+ str(num1) +" * "+ str(num2)+": ")
if result == int(guess):
    print("You're correct!")
else:
    print("Sorry! It's wrong. Correct Answer is "+str(result))
