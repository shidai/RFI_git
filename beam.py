#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import *
from matplotlib import rc

rc('text', usetex=True)

beam = np.loadtxt('beam')
xticks = np.arange(1.5,14.5)
xlabels = np.arange(1,14)
yticks = np.arange(6000000,10000000,500000)
ylabels = ('6e+06','6.5e+06','7e+06','7.5e+06','8e+06','8.5e+06','9e+06','9.5e+07')

plt.figure(figsize=(8,10), dpi=80)

ax = plt.subplot(111)
#ax1.text(0.97, 0.9, 'beam01',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
#ax1.text(0.98, 0.8, r'$f(x)\propto x^{-1.7}$',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=12)
#ax1.set_xscale("log", nonposx='clip')
#ax1.set_yscale("log", nonposy='clip')
ax.set_xlim(1,14)
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels)
ax.set_xlabel('Beam',labelpad=5,fontsize=12)
ax.set_ylabel('N',labelpad=5,fontsize=12)
ax.set_ylim(6000000,9700000)
ax.set_yticks(yticks)
ax.set_yticklabels(ylabels)
ax.plot(beam[:,0], beam[:,1])

plt.savefig('beam.ps', dpi=80)
plt.show()
