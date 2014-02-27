#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *
from matplotlib import rc

rc('text', usetex=True)

beam1 = np.loadtxt('beam01/month/result')
beam2 = np.loadtxt('beam02/month/result')
beam10 = np.loadtxt('beam10/month/result')

x = beam1[:,0]

plt.figure(figsize=(8,10), dpi=80)
gs1 = gridspec.GridSpec(3, 1)
gs1.update(left=0.08, right=0.98, top=0.95, bottom=0.06, hspace=0.1)

ax1 = plt.subplot(gs1[0, 0])
ax2 = plt.subplot(gs1[1, 0])
ax3 = plt.subplot(gs1[2, 0])

#ax1.set_title('10cm')
ax1.text(0.98, 0.9, 'beam01',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
ax1.set_xlim(0,12)
ax1.set_xticklabels([])
ax1.set_ylabel('N',labelpad=5,fontsize=12)
#ax1.set_ylim(100,10000000)
#ax1.set_yticks([100,1000,10000,100000,1000000,10000000])
#ax1.set_yticklabels([2,3,4,5,6,7])
ax1.plot(x, beam1[:,1])

ax2.text(0.98, 0.9, 'beam02',horizontalalignment='right',verticalalignment='bottom',transform=ax2.transAxes,fontsize=12)
ax2.set_xlim(0,12)
ax2.set_xticklabels([])
ax2.set_ylabel('N',labelpad=5,fontsize=12)
#ax2.set_ylim(100,10000000)
#ax2.set_yticks([100,1000,10000,100000,1000000,10000000])
#ax2.set_yticklabels([2,3,4,5,6,7])
ax2.plot(x, beam2[:,1])

ax3.text(0.98, 0.9, 'beam10',horizontalalignment='right',verticalalignment='bottom',transform=ax3.transAxes,fontsize=12)
ax3.set_xlim(0,12)
ax3.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5])
ax3.set_xticklabels(['Jan.','Feb.','Mar.','Apr.','May.','Jun.','Jul.','Aug.','Sep.','Oct.','Nov.','Dec.'])
ax3.set_xlabel('Month',labelpad=5,fontsize=12)
ax3.set_ylabel('N',labelpad=5,fontsize=12)
#ax3.set_ylim(100,10000000)
#ax3.set_yticks([100,1000,10000,100000,1000000,10000000])
#ax3.set_yticklabels([2,3,4,5,6,7])
ax3.plot(x, beam10[:,1])

plt.savefig('month.ps', dpi=80)
plt.show()
