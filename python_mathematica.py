#coding=utf-8
import os
import re
import string
import math



def  mathematica(line):
	math_file_name=''.join(map(lambda xx:(hex(ord(xx))[2:]),os.urandom(8)))
	math_file=open(math_file_name,"a")
	math_file.write(line)
	math_file.close()
	math_out=os.popen(" math -script "+math_file_name).readlines()
	os.remove(math_file_name)
	return(math_out)

print mathematica("Print[123*1236544]")