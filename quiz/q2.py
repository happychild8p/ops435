#!/usr/bin/env python3

'''Name: Heedong Yang (146191168)
	This is the documentation...
'''
def average(int_list):
   '''Calculate and return the average of a list'''
   avg = 0
   summ = 0
#	avg = 0
#	summ = 0
    ###
   for i in int_list:
       summ = summ + i
    ###
   avg = summ / len(int_list)

   return avg
if __name__ == '__main__':
    a_list = [40, 3, 4, 12, 11]
    print('Average of',a_list,'is',average(a_list))
    b_list = [20, 5, 2, 6, 2]
    print('Average of',b_list,'is',average(b_list))
    c_list = [11, 21, 31]
    print('Average of',c_list,'is',average(c_list))#!/usr/bin/env python3

