#coding:utf-8
import os
d=r"D:/computer"
def a(dir):
	if os.path.exists(dir):
		if not os.path.exists(dir):
			print  "It is a file,not a dir"
		else:
			b=[x for x in os.listdir(dir) if os.path.isfile(x) and len(os.path.splitext(x))==2 and os.path.splitext(x)[1]=='.py']
			for eachfile in b:
				print os.path.join(os.path.abspath(dir),eachfile)
			c=[x for x in os.listdir(dir) if os.path.isdir(os.path.join(os.path.abspath(dir),x))]
			for each in c:
				a(os.path.join(os.path.abspath(dir),each))
	else:
		print 'the %s does not exist' % dir
a(d)