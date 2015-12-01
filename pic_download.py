#coding:utf-8
import re
import os
import urllib
url = "http://pic.meizitu.com/wp-content/uploads/2015a/10/20/01.jpg"
def pic_download(url):
	pic_name = re.split('/',url)[-1]
	b = urllib.urlopen(url)
	a = open(pic_name,'wb')
	a.write(b.read())
	a.close()
pic_download(url)

