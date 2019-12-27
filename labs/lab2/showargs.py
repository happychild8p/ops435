#!/usr/bin/env python3

import sys

arguments = sys.argv
name = sys.argv[0]

print('Print out ALL script arguments: ', arguments)
print('Print out the script name: ' + name)
print('Print out the number of argument: ', len(sys.argv))