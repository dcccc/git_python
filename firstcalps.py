#coding:utf-8
def a(name):
	b = name
	b=b.lower()
	return b[0].upper()+b[1:]   #把首字母变大写
print map(a,['adam','LISA','barT'])
