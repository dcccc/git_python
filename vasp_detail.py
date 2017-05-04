#coding=utf-8
import math
import os
import glob


vasp_list=glob.glob("*")



print "-"*55

for out in vasp_list:
	if os.path.isdir(out) and os.path.isfile(out+"/POSCAR") :
		if os.path.isfile(out+"/out"):
			job_done = os.popen(" tail -n 1 "+out+"/out").readlines()
			if "writing wavefunctions" in job_done[0] :
				energy=os.popen("grep F= "+out+"/out | tail -n 1").readlines()
				#out_result.write("%50s%20s" %(out, energy[0][-20:]))
				print "%-30s  %20s" %(out, energy[0][7:23])
			else:
				#out_result.write("%50s%20s" %(out, "not finished yet"))
				print "%-30s  %20s" %(out, "  task not finished yet")
		else:
			print "%-30s  %20s" %(out, "  task not start yet")

print "-"*55
#out_result.close()
