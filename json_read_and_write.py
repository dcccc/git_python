#coding:utf-8
import json
import os
d='this is a string'
f=os.path.join(os.getcwd(),'12345')
a=open(f,'wb')
json.dump(d,a)
a.close()
print json.dumps(d)
f=open(f,'rb')
print json.load(f)
f.close()
