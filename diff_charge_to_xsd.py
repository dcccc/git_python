#coding=utf-8
# import math
# import random
# import sys
# import time
import numpy as np
# import matplotlib.pyplot as plt
import os, re, sys
import xml.etree.ElementTree as etree  
import linecache

xsd=open(sys.argv[1],"r")

tree = etree.parse(xsd)
Atom3d_list=tree.findall("AtomisticTreeRoot/SymmetrySystem/MappingSet/MappingFamily/IdentityMapping/Atom3d")


charge=[]
for i in open(sys.argv[2]):
	charge.append(i.strip())
# print charge
for i, atom in enumerate(Atom3d_list):
	atom.attrib["Charge"]=charge[i]
	# print atom.attrib["ID"]
tree.write(sys.argv[1][:-4]+"_charge.xsd", encoding="utf-8",xml_declaration=True)

