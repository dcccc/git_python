#coding=utf-8
'''
import multiprocessing as mul
  
def f(x):
    return x**2
if __name__ == '__main__':
    pool = mul.Pool(5)
    rel  = pool.map(f,[1,2,3,4,5,6,7,8,9,10])
    print(rel) 



from Tkinter import *
# -*- coding: cp936 -*-
from Tkinter import *
root = Tk()
root.title("hello world")
root.geometry()

def printhello():
    t.insert('1.0', "hello\n")
    
t = Text()
t.pack()
Button(root, text="press", command = printhello).pack()
root.mainloop()

'''

from PIL import Image
import numpy as np
import random

a=np.arange(10000).reshape(100,100)

for i in xrange(100):
	for j in xrange(100):
		a[i,j]=random.choice([255,1])

p = Image.fromarray(a)
p=p.convert('L')
p.save("1.jpg")