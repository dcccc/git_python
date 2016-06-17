#coding=utf-8
import math
import os
import glob


pw_list=glob.glob("*.in")

#out_result=open("pw_out_result.txt","a")

print "-"*55

for out in pw_list:
	out=out[:-3]+".out"
	if os.path.isfile(out):
		job_done = os.popen(" tail -n 2 "+out).readlines()
		if "JOB DONE" in job_done[0] :
			energy=os.popen("grep ! "+out+" | tail -n 1").readlines()
			#out_result.write("%50s%20s" %(out, energy[0][-20:]))
			print "%-30s  %20s" %(out[:-4], energy[0][-20:-1])
		else:
			#out_result.write("%50s%20s" %(out, "not finished yet"))
			print "%-30s  %20s" %(out[:-4], "  task not finished yet")
	else:
		print "%-30s  %20s" %(out[:-3], "  task not start yet")

print "-"*55
#out_result.close()

