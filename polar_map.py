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
#data = np.loadtxt('azimuth_beam01_new')
data = np.loadtxt('azimuth_result')

azimuth = np.arange(0,np.pi*2,np.pi*2/360)
#azimuth = linspace(0,360,360)
#r = np.arange(1,90)
r = np.cos(data[0:90,1]*np.pi/180)

(m,n) = data.shape
for i in np.arange(0,m):
	if data[i,3] != 0:
		data[i,2] = data[i,2]/data[i,3]

#val = np.rot90(np.reshape(data[:,2],(360,90)))
val = np.flipud(np.rot90(np.reshape(data[:,2],(360,90))))

# Create a polar axes
#ax = plt.subplot(111)
#ax = plt.subplot(111, polar=True)
ax = plt.subplot(111, projection='polar')

ax.set_yticks([0.5,0.866])
ax.set_yticklabels([r'$60^{\circ}$',r'$30^{\circ}$'])

ax.set_xticks(np.arange(0,np.pi*2,np.pi/8))
ax.set_xticklabels([r'$0^{\circ}$','',r'$45^{\circ}$','', r'$90^{\circ}$','', r'$135^{\circ}$','',r'$180^{\circ}$','',r'$225^{\circ}$','',r'$270^{\circ}$','',r'$315^{\circ}$',''])

ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.text(0.45, 0.45, 'Zenith',horizontalalignment='center',verticalalignment='center',transform=ax.transAxes,fontsize=12)
# pcolor plot onto it
#ax.pcolor(azimuth, r, val, cmap='binary', vmin=0, vmax=1000)
ax.pcolor(azimuth, r, val, cmap='YlOrBr', vmin=0, vmax=100)

#plt.minorticks_on()
plt.grid()
plt.savefig("azimuth_beam01.ps",dpi=200)
plt.show()
