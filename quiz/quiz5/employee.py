#!/usr/bin/env python3
'''
 Student Name = Heedong Yang 
 Student number = 146191168
 Student Email = hyang117@myseneca.ca
 OPS435 Quiz 5
 Question 2
 employee.py
'''
class Prof:

    def __init__(self, name, eid, campus):
        self.name = name
        self.id = eid
        sites = ['Newnham', 'King', 'Seneca@York', 'Markham', 'Peterborough']
        if campus in sites:
            self.campus = campus
        else:
            self.campus = 'Seneca'

    def displayInfo(self):
        result = 'Professor Name: '
        result += self.name
        result += '\n\n'
        result += 'Employee ID: '
        result += self.id
        result += '\n\n'
        result += 'Campus: '
        result += self.campus

        return result

    	


