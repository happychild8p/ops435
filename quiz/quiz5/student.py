#!/usr/bin/env python3
'''
 Student Name = Heedong Yang 
 Student number = 146191168
 Student Email = hyang117@myseneca.ca
 OPS435 Quiz 5
 Question 1
 student.py

'''

class Student:

     def __init__(self, name, number, program):
         programs = ['CNS', 'CTY']
         self.name = name
         self.number = number
         self.courses = {}

         if program in programs:
             self.program = program
         else:
             self.program = 'unknown'

     def displayStudent(self):
         result = 'Name: '
         result += self.name
         result += '\n\n'
         result += 'ID No: '
         result += self.number
         result += '\n\n'
         result += 'Program: '
         result += self.program
         return result

