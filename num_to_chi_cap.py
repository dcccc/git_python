#coding=utf-8
import re
import math
num_chi = ["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
num_dig = ["","拾","佰","仟","万","亿"]


def f_wan(num , num_cap = ""):
	for i in range(len(num)):
			num_cap = num_cap + num_chi[int(num[i])]+ " " + num_dig[len(num)-1-i]+ " "
	return num_cap

def f_yi(num , num_cap = ""):
	if len(num) > 4:
		num_cap = f_wan(num[0:len(num)-4])+ " "  + num_dig[4] + " " + f_wan(num[len(num)-4:])+ " " 
	else:
		num_cap = f_wan(num[:])
	return num_cap


def f_yiyi(num , num_cap = ""):
	if len(num) > 8:
		num_cap = f_yi(num[:len(num)-8])+ " "  + num_dig[5]+ " "  + f_yi(num[len(num)-8:])		
	else:
		num_cap = f_yi(num[:])
	return num_cap

def f(num , num_cap = ""):
	num_cap = f_yiyi(num)
	num_capp = re.split("\s+",num_cap)
	del num_capp[-1]
	num_capp_join = "".join(num_capp)
	len_aft = 0
	while len(num_capp) != len_aft :
		len_aft = len(num_capp)
		#print len_aft
		for i in range(len(num_capp)-1):
			if i <= len(num_capp)-2:
				if num_capp[i] == "零" :
					if num_capp[i+1] == "拾" or num_capp[i+1] == "佰" or num_capp[i+1] == "仟":
						del num_capp[i+1]
					elif num_capp[i+1] == "万" or num_capp[i+1] == "亿" :
						del num_capp[i]

	#num_capp_join = "".join(num_capp)
	#print num_capp_join
	while "零零" in num_capp_join:
		for i in range(len(num_capp)-1):
			if i <= len(num_capp)-1 and num_capp[i] == "零" and num_capp[i+1] == "零" :
				del num_capp[i]
		num_capp_join = "".join(num_capp)
	print num_capp_join
	for i in range(len(num_capp)-1):
			if i <= len(num_capp)-1:
				if  num_capp[i] == "万"  and num_capp[i+1] == "亿":
					del num_capp[i+1]
#				if  num_capp[i] == "亿"  and num_capp[i+1] == "万":
#					del num_capp[i+1]

	while num_capp[-1] == "零" :
		del num_capp[-1]

	return "".join(num_capp)


h=open(r"C:\Users\dcc\Desktop\test.txt",'a')
h.write(f("1000000000"))





"""
num=str(num)

if length2 > 1 :B
	for i in range(length-8):
		num_cap = num_chi[i] + num_dig[i]
"""