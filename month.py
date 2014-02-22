#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib import rc

rc('text', usetex=True)

#######################################################
#from pylab import *
# Sampling 60 points in both dimensions
#T = linspace(0, np.pi * 2, 360)
#R = linspace(0, 1.0, 60)
#Z = rand(60,360)

# Create a polar axes
#ax = subplot(111, projection='polar')
# pcolor plot onto it
#c = ax.pcolor(T, R, Z)
#title('default: no edges')
#show()
#######################################################

# read data
data = np.loadtxt('month')
norm = np.loadtxt('month_norm_beam1')
month = data[:,0]
value = data[:,1]
num = [0,0,0,0,0,0,0,0,0,0,0,0]
#norm = [0,0,0,0,0,0,0,0,0,0,0,0]

(m,n) = data.shape

for i in np.arange(0,m):
	for j in np.arange(0,12):
		if month[i] == j+1:
			num[j] = num[j] + value[i]
#			norm [j] = norm[j] + 1

for j in np.arange(0,12):
	num[j] = num[j]/norm[j]
	print j, num[j]
	print j+1, num[j]

#print norm
'''
ax = plt.subplot(111)

ax.set_yticks([0.5,0.866])
ax.set_yticklabels([r'$60^{\circ}$',r'$30^{\circ}$'])

ax.set_xticks(np.arange(0,np.pi*2,np.pi/8))
ax.set_xticklabels([r'$0^{\circ}$','',r'$45^{\circ}$','', r'$90^{\circ}$','', r'$135^{\circ}$','',r'$180^{\circ}$','',r'$225^{\circ}$','',r'$270^{\circ}$','',r'$315^{\circ}$',''])

ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.text(0.45, 0.45, 'Zenith',horizontalalignment='center',verticalalignment='center',transform=ax.transAxes,fontsize=12)
# pcolor plot onto it
#ax.pcolor(azimuth, r, val, cmap='binary', vmin=0, vmax=1000)
ax.pcolor(azimuth, r, val, cmap='YlOrBr', vmin=0, vmax=2000)

#plt.minorticks_on()
plt.grid()
plt.show()
'''
