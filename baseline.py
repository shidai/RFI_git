#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec


beam1 = np.loadtxt('beam01/basic/basic.txt')
beam2 = np.loadtxt('beam02/basic/basic.txt')
beam10 = np.loadtxt('beam10/basic/basic.txt')

(m1,n1) = beam1.shape
(m2,n2) = beam2.shape
(m10,n10) = beam10.shape

x1 = np.arange(0,m1)
x2 = np.arange(0,m2)
x10 = np.arange(0,m10)

plt.figure(figsize=(8,10), dpi=80)
gs1 = gridspec.GridSpec(3, 1)
gs1.update(left=0.08, right=0.98, top=0.95, bottom=0.05, hspace=0.1)

ax1 = plt.subplot(gs1[0, 0])
ax2 = plt.subplot(gs1[1, 0])
ax3 = plt.subplot(gs1[2, 0])

#ax1.set_title('10cm')
ax1.text(0.98, 0.9, 'beam01',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
#ax1.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax1.set_xlim(-10000,420000)
ax1.set_xticklabels([])
#ax1.set_ylabel('PA (deg)',labelpad=0)
ax1.set_ylim(-10000,130000)
ax1.set_yticklabels([])
#ax1.set_yticks([10,40,70])
#ax1.set_xlim(-0.2,0.2)
ax1.plot(x1, beam1[:,1],'r+')

ax2.text(0.98, 0.9, 'beam02',horizontalalignment='right',verticalalignment='bottom',transform=ax2.transAxes,fontsize=12)
ax2.set_xlim(-10000,420000)
ax2.set_xticklabels([])
ax2.set_ylabel('Meam flux of each data block',labelpad=5)
ax2.set_ylim(-10000,70000)
ax2.set_yticklabels([])
ax2.plot(x2, beam2[:,1],'r+')

ax3.text(0.98, 0.9, 'beam10',horizontalalignment='right',verticalalignment='bottom',transform=ax3.transAxes,fontsize=12)
ax3.set_xlim(-10000,420000)
#ax3.set_xticklabels([])
ax3.set_ylim(-10000,130000)
ax3.set_yticklabels([])
ax3.plot(x10, beam10[:,1],'r+')

plt.savefig('baseline.ps', dpi=80)
plt.show()
