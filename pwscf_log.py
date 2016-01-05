#!/usr/bin/python
#coding:utf-8
import os
import re
import glob
import sys
import linecache
import time

def task_detail():
	pw=sorted(os.popen("top -b -n 1 | grep pw.x").readlines())
	user,task_name = [],[]
	for i in range(0,len(pw),4):
		line = re.split(r'\s+',pw[i].lstrip().rstrip())
		user.append(line[1])

		pid_of=os.popen("lsof -p"+line[0]+" | grep /home/").readlines()
		cwd = re.split(r'\s+',pid_of[0].lstrip().rstrip())[-1]
		task= re.split(r'\/',pid_of[-1].lstrip().rstrip())[-1]
		#task = re.match(r"",task)
		task = task.replace("igk","in")
		task_name.append(cwd+"/"+task)
	return(user,task_name)

pwscf_log=open("/home/flw/pwscf_log","a")
user1,task_name1 = [],[]
while ( True ) :
	(user,task_name) = task_detail()
	if task_name1 == task_name :
		time.sleep(60)
	else :
		task_name_join = "".join(task_name)
		task_name1_join = "".join(task_name1)
		for i,line in enumerate(task_name) :
			if line in task_name1_join :
				pass
			else :
				pwscf_log.write("-----------------------------------\n")
				times=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
				pwscf_log.write("At time "+ times+"\n")
				pwscf_log.write(user[i] + "        "+ line + " starts.\n\n\n")
		for i,line in enumerate(task_name1) :
			if line in task_name_join :
				pass
			else :
				pwscf_log.write("***********************************\n")
				times=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
				pwscf_log.write("At time "+ times+"\n")
				pwscf_log.write(user1[i] + "        "+ line + " finishs.\n\n\n")

	if time.strftime("%H:%M",time.localtime(time.time())) == "00:00":
		times=time.strftime("%Y-%m-%d",time.localtime(time.time()))
		pwscf_log.write("########## "+times+" ###################################\n\n")

	pwscf_log.flush()
	task_name1 = task_name



