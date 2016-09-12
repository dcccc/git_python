#coding=utf-8
import re
import math
import sys

reload(sys)
sys.setdefaultencoding("utf-8")

num_chi = [u"零",u"壹",u"贰",u"叁",u"肆",u"伍",u"陆",u"柒",u"捌",u"玖"]
num_dig = ["",u"拾",u"佰",u"仟",u"万",u"亿"]

def f_wan(num):
	num_cap=u''
	for i in range(len(num)):
			num_cap = num_cap + num_chi[int(num[i])]+ num_dig[len(num)-1-i]
	return num_cap

def f_yi(num):
	num_cap=u''
	if len(num)>4 :
		num_cap=f_wan(num[:-4])+u"万"+f_wan(num[-4:])
	else :
		num_cap=f_wan(num)
	return num_cap

def f_yiyi(num):
	num_cap=u''
	if len(num)>8 :
		num_cap=f_yi(num[:-8])+u"亿"+f_yi(num[-8:])
	else :
		num_cap=f_yi(num)
	return num_cap

def inte(num):
	num_cap=f_yiyi(num)
	num_cap = re.sub(ur'\u96f6[\u62fe\u4f70\u4edf]', ur"\u96f6", num_cap)
	num_cap = re.sub(ur'\u96f6\u4e07', ur"\u4e07\u96f6", num_cap)
	num_cap = re.sub(ur'\u96f6\u4ebf', ur"\u4ebf\u96f6", num_cap)
	num_cap = re.sub(ur'\u96f6{2,}', ur"\u96f6", num_cap)
	if len(num_cap) != 1:
		num_cap = re.sub(ur'\u96f6$', ur"", num_cap)
	return num_cap


def deci(dec):
	num_cap = u""
	for i in range(len(dec)):
		num_cap = num_cap + num_chi[int(dec[i])]
	return num_cap

def num_2_chi(num):
	num_ = re.split(r'\.' , num)
	if len(num_) == 2:
		return inte(num_[0]) +u"点" + deci(num_[1])
	elif len(num_) == 1 :
		return inte(num_[0])
	else :
		print "the number is wrong!"
		sys.exit()

def num_2_frac(num):
	num_ = re.split(r'\/' , num)
	if len(num_) == 2:
		return num_2_chi(num_[1]) +u"分之" + num_2_chi(num_[0])
	else :
		print "the number is wrong!"
		sys.exit()



print num_2_frac("111.1/231.52")