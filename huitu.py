#coding=utf-8
import math
import random
import sys
import numpy as np
import matplotlib.pyplot as plt

data=np.genfromtxt("plane.txt")

def f(x,y):
	return data[x,y]

x=np.arange(200)
y=np.arange(200)


B=plt.contourf(data, 16, alpha=.75, cmap='jet')
C = plt.contour(data, 16, colors='black', linewidth=.5)
plt.clabel(C, inline=1, fontsize=10)
plt.colorbar(B, shrink=0.8, extend='both')
plt.show()