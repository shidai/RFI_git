#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *
from matplotlib import rc

rc('text', usetex=True)

beam1 = np.loadtxt('beam01/occurrance/result')
beam2 = np.loadtxt('beam02/occurrance/result')
beam10 = np.loadtxt('beam10/occurrance/result')

x = beam1[:,0]

plt.figure(figsize=(8,10), dpi=80)
gs1 = gridspec.GridSpec(3, 1)
gs1.update(left=0.08, right=0.98, top=0.95, bottom=0.06, hspace=0.1)

ax1 = plt.subplot(gs1[0, 0])
ax2 = plt.subplot(gs1[1, 0])
ax3 = plt.subplot(gs1[2, 0])

ticks=np.arange(0,48,2)
#ax1.set_title('10cm')
ax1.text(0.98, 0.9, 'beam01',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
ax1.set_xlim(0,48)
ax1.set_xticks(ticks)
ax1.set_xticklabels([])
ax1.set_ylabel('N',labelpad=5,fontsize=12)
#ax1.set_ylim(100,10000000)
#ax1.set_yticks([100,1000,10000,100000,1000000,10000000])
#ax1.set_yticklabels([2,3,4,5,6,7])
ax1.plot(x, beam1[:,1])

ax2.text(0.98, 0.9, 'beam02',horizontalalignment='right',verticalalignment='bottom',transform=ax2.transAxes,fontsize=12)
ax2.set_xlim(0,48)
ax2.set_xticks(ticks)
ax2.set_xticklabels([])
ax2.set_ylabel('N',labelpad=5,fontsize=12)
#ax2.set_ylim(100,10000000)
#ax2.set_yticks([100,1000,10000,100000,1000000,10000000])
#ax2.set_yticklabels([2,3,4,5,6,7])
ax2.plot(x, beam2[:,1])

ax3.text(0.98, 0.9, 'beam10',horizontalalignment='right',verticalalignment='bottom',transform=ax3.transAxes,fontsize=12)
ax3.set_xlim(0,48)
label=np.arange(0,24)
ax3.set_xticks(ticks)
ax3.set_xticklabels(label)
ax3.set_xlabel('Local time',labelpad=5,fontsize=12)
ax3.set_ylabel('N',labelpad=5,fontsize=12)
#ax3.set_ylim(100,10000000)
#ax3.set_yticks([100,1000,10000,100000,1000000,10000000])
#ax3.set_yticklabels([2,3,4,5,6,7])
ax3.plot(x, beam10[:,1])

plt.savefig('occurrence.ps', dpi=80)
plt.show()
