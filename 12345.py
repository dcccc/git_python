#coding:utf-8
import re
print re.split('[\s\,]','a a,b')
a=re.match('^([0-9]{4})\s([0-9]{4}\s[0-9]{4})\s([0-9]{4})\s([0-9]{3})$','6217 0028 7000 2338 174')
print a.groups()
re.match(r'^(\d+?)(0*)$', '102300').groups()  #  ?表示该匹配语句尽量少匹配  不影响后面的匹配

import hashlib
md5=hashlib.md5()
md5.update('this is a string')
print md5.hexdigest()