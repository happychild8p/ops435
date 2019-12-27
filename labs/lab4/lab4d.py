#!/usr/bin/env python3

# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(str1):
    # Place code here - refer to function specifics in section below
    return str1[0:5]
def last_seven(str2):
    return str2[-7:]
    # Place code here - refer to function specifics in section below
def middle_number(num1):
    # Place code here - refer to function specifics in section below
    abc=str(num1)
    return abc[1:3]
def first_three_last_three(a, b):
    # Place code here - refer to function specifics in section below
    aa = str(a)
    bb = str(b)
    return aa[:3]+bb[-3:]

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))