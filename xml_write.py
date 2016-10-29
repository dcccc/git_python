#coding=utf-8
# import math
# import random
# import sys
# import time
import numpy as np
# import matplotlib.pyplot as plt
import os, re  
import xml.etree.ElementTree as etree  

xsd=open("LiFePO4_2_2.pw.xsd","r")

tree = etree.parse(xsd)
root = tree.getroot()
# print root.attrib
Atom3d_list=tree.findall("AtomisticTreeRoot/SymmetrySystem/MappingSet/MappingFamily/IdentityMapping/Atom3d")

for atom in Atom3d_list:
	atom.attrib["Charge"]="0.25"
tree.write("out.xsd", encoding="utf-8",xml_declaration=True)