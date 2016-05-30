#coding=utf-8
import re
import glob



def to_md(enw):
	article=[]
	file=open(enw)
	for i, line in enumerate(file):
		article.append(line[3:].strip())
	
	#print article
	Au_num=0
	for i in xrange(len(article)):
		if "," in article[i]:
			Au=re.split(r'\,\s',article[i])
			Au[1]=re.sub(r'[a-z]+','',Au[1])
			article[i]= " ".join(Au)
			Au_num+=1

	
	md_txt= "%s. %s[%s]. *%s*, %s, %s(%s): %s."    %(", ".join(article[2:Au_num+2]), article[1], article[0][0],    
	                                     article[Au_num+2], article[Au_num+7], article[Au_num+3],  article[Au_num+4], article[Au_num+5])
	return md_txt

txt=open("markdown.md","a")

all_enw=glob.glob("*.enw")

print all_enw
for i in all_enw:
	print to_md(i)