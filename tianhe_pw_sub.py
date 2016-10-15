#coding=utf-8
import math
import random
import glob
import sys
import os
if len(sys.argv) == 2:
	n=sys.argv[1]
else:
	print("process number should be inputed")
	sys.exit()

pw_task = glob.glob("*.in")

for i in pw_task:
	sh_txt=open(i[:-5]+"sh","a")
	txt= "#!/bin/bash\nyhrun -N 1 -n %s pw.x < %s >& %s" %(n, i, i[:-2]+"out")
	sh_txt.write(txt)
	sh_txt.close()

	os.popen("chmod +x  *.sh").readlines()
