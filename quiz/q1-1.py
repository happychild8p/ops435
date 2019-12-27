#!/usr/bin/env python3

ccb_u6 = 541
ccb_6to17 = 456

child_u6 = input("What is the number of child under the age of 6?")
child_6to17 = input("What is the number of child aged 6 to 17?")

ccb_total = (int(ccb_u6) * int(child_u6)) + (int(ccb_6to17) * int(child_6to17))

print("The total Canada Child Benefit for the family is " + str(ccb_total))

