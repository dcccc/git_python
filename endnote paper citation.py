#coding=utf-8
import math
import random
import sys
import time
import numpy as np
import re

file=open("scholar.enw")


article=[]
for i, line in enumerate(file):
	article.append(line[3:].strip())

#print article
for i in [2,3,4]:
	Au=re.split(r'\,\s',article[i])
	Au[1]=re.sub(r'[a-z]+','',Au[1])
	article[i]= " ".join(Au)

print "%s. %s[%s]. *%s*, %s, %s(%s): %s."    %(", ".join(article[2:5]), article[1], article[0][0],    
                                            article[5], article[9], article[6],  article[7], article[8])
