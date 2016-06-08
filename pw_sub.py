#coding=utf-8
import math
import random
import glob
import sys

if len(sys.argv) >1:
	pro_num=sys.argv[1]
else:
	print("process number should be inputed")
	sys.exit()

pw_task = glob.glob("*.in")

n=3
file_num= len(pw_task) / n+1

if len(pw_task) >0:
	for script_num in xrange(n):
		task_script_name = "task_script_%d.sh" %(script_num+1)
		task_script = open(task_script_name,'a')
		task_script.write("#!/bin/sh\n")

		i=file_num*script_num
		while (i < file_num*(script_num+1) and i >= file_num*script_num):
			command_line = "mpirun -np %s pw.x < %s.in > %s.out\n"  %(pro_num, pw_task[i][:-3], pw_task[i][:-3])
			task_script.write(command_line)
			i+=1
			if i >= len(pw_task):
				sys.exit()
		task_script.close()
else:
	print("No pwscf input file in the diretory!")