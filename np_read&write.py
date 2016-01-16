#coding:utf-8
import numpy as np
a = np.arange(1,201).reshape(10,20)
#np.savetxt("a.txt", a)    #保存为txt格式 缺省按照'%.18e'格式保存数值 以空格分隔
#np.savetxt("a.txt", a, fmt="%d", delimiter=",")   #保存为保存为整数，以逗号分隔
#np.loadtxt("a.txt")       #读取txt格式的数据
#np.loadtxt("a.txt",delimiter=",") # 读入的时候也需要指定逗号分隔

#a.tofile("a")             #保存到文件中   二进制格式  
#b = np.fromfile("a", dtype=np.int32)   #读取文件   需要指定数据类型

#np.save("c.npy", a)    #专用的二进制格式保存数据，它们会自动处理元素类型和形状等信息
c = np.load( "c.npy" )

np.savez("result.npz", a, a, sin_array = a)  #可以使用savez() 将多个数组保存到一个文件中
r = np.load("result.npz")  #读取数组

genfromtxt("bands.xmgr")   #自动处理格式问题  读取txt
numpy.recfromcsv()         #自动处理格式问题  读取csv

