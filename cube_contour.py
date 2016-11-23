import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons
from matplotlib.contour import QuadContourSet
import linecache
import re ,os

cubefile="LiFePO4.cube"
fft=[]

for i in [3,4,5,6]:
	line=linecache.getline(cubefile, i)
	line=re.split(r'\s',line.strip())
	fft.append(int(line[0]))

data=[]
num_line=fft[0]+7
while(linecache.getline(cubefile , num_line)):
	line=linecache.getline(cubefile , num_line)
	line=map(float,re.split(r'\s+',line.strip()))
	data.extend(line)
	num_line+=1
data=np.array(data).reshape(fft[3],fft[2],fft[1])

fig, ax = plt.subplots()
B=plt.contourf(data[:,:,2], 16, alpha=.75, cmap='jet')

samp=plt.axes([0.25, 0.01, 0.5, 0.03])
axfreq = plt.axes([0.125, 0.1, 0.82, 0.82], axisbg='lightgoldenrodyellow')
sfreq = Slider(axfreq,"",0, 100.0, valfmt="%d",valinit=0)
samp = Slider(samp,"z",0, 100.0, valfmt="%d",valinit=0)


def update(ax,val):
    freq = sfreq.val
    ax.cla()
    # plt.contourf(data[:,:,int(val)], 16, alpha=.75, cmap='jet')
    B=plt.contourf(data[:,:,int(val)], 16, alpha=.75, cmap='jet')
    # C=plt.contour(data[:,:,int(val)], 16, colors='black', linewidth=.5)
    # plt.clabel(C, inline=1, fontsize=10)
    # plt.colorbar(B, shrink=0.8, extend='both')

samp.on_changed(lambda val: update(ax,val))

plt.show()
#QuadContourSet(ax,data[:,:,int(val)],200)