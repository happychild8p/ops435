#!/usr/bin/env python3

import subprocess

def free_space():
	p = subprocess.Popen(["df -h | grep '/$' | awk '{print $4}'"],stdin=None,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
	result = p.communicate()
	output = result[0].decode('utf-8').strip()
	error = result[1].decode('utf-8').strip()
	return output

if __name__=="__main__":
	a = free_space()
	print(a)
