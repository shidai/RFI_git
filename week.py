#!/usr/bin/env python

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
from matplotlib import rc
import datetime

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

# read norm
ndata = np.loadtxt('norm')
nyear = ndata[:,0]
nmonth = ndata[:,1]
nday = ndata[:,2]
nhour = ndata[:,3]
nvalue = ndata[:,4]
ntimeleg = ndata[:,5]

norm = [0,0,0,0,0,0,0]

(h,k) = ndata.shape

for i in np.arange(0,h):
	if nhour[i] + ntimeleg[i] >= 24:
		nday[i] = nday[i] + 1
	
	if nmonth[i] == 1 or nmonth[i] == 3 or nmonth[i] == 5 or nmonth[i] == 7 or nmonth[i] == 8 or nmonth[i] == 10 or nmonth[i] == 12:
		if nday[i] > 31:
			nday[i] = nday[i] - 31
			nmonth[i] = nmonth[i] + 1
	elif nmonth[i] == 2:
		if nday[i] > 28:
			nday[i] = nday[i] - 28
			nmonth[i] = nmonth[i] + 1
	else:
		if nday[i] > 30:
			nday[i] = nday[i] - 30
			nmonth[i] = nmonth[i] + 1

	if nmonth[i] > 12:
		nmonth[i] = nmonth[i] - 12
		nyear[i] = nyear[i] + 1

	ndt = datetime.date((int)(nyear[i]), (int)(nmonth[i]), (int)(nday[i]))
	nwk = ndt.isocalendar()[2]

	for j in np.arange(0,7):
		if nwk == j+1:
			norm[j] = norm[j] + nvalue[i]

# read data
data = np.loadtxt('week')
year = data[:,0]
month = data[:,1]
day = data[:,2]
hour = data[:,3]
value = data[:,6]
timeleg = data[:,7]

num = [0,0,0,0,0,0,0]

(m,n) = data.shape

for i in np.arange(0,m):
	if hour[i] + timeleg[i] >= 24:
		day[i] = day[i] + 1
	
	if month[i] == 1 or month[i] == 3 or month[i] == 5 or month[i] == 7 or month[i] == 8 or month[i] == 10 or month[i] == 12:
		if day[i] > 31:
			day[i] = day[i] - 31
			month[i] = month[i] + 1
	elif month[i] == 2:
		if day[i] > 28:
			day[i] = day[i] - 28
			month[i] = month[i] + 1
	else:
		if day[i] > 30:
			day[i] = day[i] - 30
			month[i] = month[i] + 1

	if month[i] > 12:
		month[i] = month[i] - 12
		year[i] = year[i] + 1

	dt = datetime.date((int)(year[i]), (int)(month[i]), (int)(day[i]))
	wk = dt.isocalendar()[2]

	for j in np.arange(0,7):
		if wk == j+1:
			num[j] = num[j] + value[i]
#			norm [j] = norm[j] + 1

for j in np.arange(0,7):
	print j, num[j]/norm[j]
	print j+1, num[j]/norm[j]

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
