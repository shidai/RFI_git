#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *
from matplotlib import rc

rc('text', usetex=True)

x = np.arange(0,4,0.1)
y = 10**(-1.8*x+6.6)

beam1 = np.loadtxt('beam01/width/result_log')
beam2 = np.loadtxt('beam02/width/result_log')
beam10 = np.loadtxt('beam10/width/result_log')

plt.figure(figsize=(8,10), dpi=80)
gs1 = gridspec.GridSpec(3, 1)
gs1.update(left=0.08, right=0.98, top=0.95, bottom=0.06, hspace=0.1)

ax1 = plt.subplot(gs1[0, 0])
ax2 = plt.subplot(gs1[1, 0])
ax3 = plt.subplot(gs1[2, 0])

#ax1.set_title('10cm')
ax1.text(0.97, 0.9, 'beam01',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
ax1.text(0.98, 0.8, r'$f(x)\propto x^{-1.8}$',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
#ax1.set_xscale("log", nonposx='clip')
ax1.set_yscale("log", nonposy='clip')
ax1.set_xlim(0,3)
ax1.set_xticklabels([])
ax1.set_ylabel(r'$log_{10}(N)$',labelpad=5,fontsize=12)
ax1.set_ylim(1,10000000)
ax1.set_yticks([100,10000,1000000])
ax1.set_yticklabels([2,4,6])
ax1.plot(beam1[:,0], beam1[:,1])
ax1.plot(x, y, 'r--')

ax2.text(0.97, 0.9, 'beam02',horizontalalignment='right',verticalalignment='bottom',transform=ax2.transAxes,fontsize=12)
ax2.text(0.98, 0.8, r'$f(x)\propto x^{-1.8}$',horizontalalignment='right',verticalalignment='bottom',transform=ax2.transAxes,fontsize=12)
#ax2.set_xscale("log", nonposx='clip')
ax2.set_yscale("log", nonposy='clip')
ax2.set_ylabel(r'$log_{10}(N)$',labelpad=5)
ax2.set_xlim(0,3)
ax2.set_xticklabels([])
ax2.set_ylabel(r'$log_{10}(N)$',labelpad=5,fontsize=12)
ax2.set_ylim(1,10000000)
ax2.set_yticks([100,10000,1000000])
ax2.set_yticklabels([2,4,6])
ax2.plot(beam2[:,0], beam2[:,1])
ax2.plot(x, y, 'r--')

ax3.text(0.97, 0.9, 'beam10',horizontalalignment='right',verticalalignment='bottom',transform=ax3.transAxes,fontsize=12)
ax3.text(0.98, 0.8, r'$f(x)\propto x^{-1.8}$',horizontalalignment='right',verticalalignment='bottom',transform=ax3.transAxes,fontsize=12)
#ax3.set_xscale("log", nonposx='clip')
ax3.set_yscale("log", nonposy='clip')
ax3.set_xlim(0,3)
ax3.set_xticks([0,1,2,3])
#ax3.set_xticklabels([0.02,0.1,1])
ax3.set_xlabel(r'$log_{10}(W)\ (\rm{64 \mu s})$',labelpad=5,fontsize=12)
ax3.set_ylabel(r'$log_{10}(N)$',labelpad=5,fontsize=12)
ax3.set_ylim(1,10000000)
ax3.set_yticks([100,10000,1000000])
ax3.set_yticklabels([2,4,6])
ax3.plot(beam10[:,0], beam10[:,1])
ax3.plot(x, y, 'r--')

plt.savefig('width.ps', dpi=80)
plt.show()
