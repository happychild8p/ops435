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
def append_file_string(file_name, string_of_lines):
    # Takes two strings, appends the string to the end of the file
    f = open(file_name, 'a')
    line_list = string_of_lines.split('\n')
    for line in line_list[:-1]:
        f.write(str(line)+'\n')
    f.close()

def write_file_list(file_name, list_of_lines):
    # Takes a string and list, writes all items from list to file where each
    # item is one line
    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(str(line)+'\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    # Takes two strings, reads data from first file, writes data to new 
    #file, adds line number to new file
    f1 = open(file_name_read, 'r')
    f2 = open(file_name_write, 'w')
    list1 = f1.read().split('\n')
    num = 1
    for line in list1[:-1]:
        f2.write(str(num)+':'+str(line)+'\n')
        num += 1
    f1.close()
    f2.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']
    append_file_string(file1, string1)
    print(read_file_string(file1))
    write_file_list(file2, list1)
    print(read_file_string(file2))
    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))