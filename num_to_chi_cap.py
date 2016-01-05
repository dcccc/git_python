#coding=utf-8
import re
import math
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
num_chi = [u"零",u"壹",u"贰",u"叁",u"肆",u"伍",u"陆",u"柒",u"捌",u"玖"]
num_dig = ["",u"拾",u"佰",u"仟",u"万",u"亿"]


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
				if num_capp[i] == u"零" :
					if num_capp[i+1] == u"拾" or num_capp[i+1] == u"佰" or num_capp[i+1] == u"仟":
						del num_capp[i+1]
					elif num_capp[i+1] == u"万" or num_capp[i+1] == u"亿" :
						del num_capp[i]

	#num_capp_join = "".join(num_capp)
	#print num_capp_join
	while u"零零" in num_capp_join:
		for i in range(len(num_capp)-1):
			if i <= len(num_capp)-1 and num_capp[i] == u"零" and num_capp[i+1] == u"零" :
				del num_capp[i]
		num_capp_join = "".join(num_capp)
	#print num_capp_join
	for i in range(len(num_capp)-1):
			if i <= len(num_capp)-1:
				if  num_capp[i] == u"亿"  and num_capp[i+1] == u"万":
					del num_capp[i+1]
#				if  num_capp[i] == "亿"  and num_capp[i+1] == "万":
#					del num_capp[i+1]
	num_capp_join = "".join(num_capp)
	while u"零零" in num_capp_join:
		for i in range(len(num_capp)-1):
			if i <= len(num_capp)-1 and num_capp[i] == u"零" and num_capp[i+1] == u"零" :
				del num_capp[i]
		num_capp_join = "".join(num_capp)

	while num_capp[-1] == u"零" and len(num_capp) != 1 :
		del num_capp[-1]

	return "".join(num_capp)

def deci(dec):
	num_capp = ""
	for i in range(len(dec)):
		num_capp = num_capp + num_chi[int(dec[i])]
	return num_capp

def num_chi_cap(num):
	num_ = re.split(r'\.' , num)
	if len(num_) == 2:
		return f(num_[0]) +u"点" + deci(num_[1])
	elif len(num_) == 1 :
		return f(num_[0])
	else :
		print "the number is wrong!"
		sys.exit()

	



#h=open(r"C:\Users\dcc\Desktop\test.txt",'a')
#h.write(f("100000000000000"))
print num_chi_cap("100010010001.11")
