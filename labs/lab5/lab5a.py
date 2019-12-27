#!/usr/bin/env python3

def read_file_string(file_name):
    # Takes a filename string, returns a string of all lines in the file
    f = open(file_name, 'r')
    return f.read()
def read_file_list(file_name):
    # Takes a filename string, returns a list of lines without new-line characters
    f = open(file_name, 'r')
    lines = f.read().split('\n')
    return lines[:-1]
if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))