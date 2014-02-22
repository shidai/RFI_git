#!/usr/bin/python

import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib import rc

rc('text', usetex=True)

jan = np.loadtxt('1/result_norm')
fab = np.loadtxt('2/result_norm')
mar = np.loadtxt('3/result_norm')
apr = np.loadtxt('4/result_norm')
may = np.loadtxt('5/result_norm')
jun = np.loadtxt('6/result_norm')
jul = np.loadtxt('7/result_norm')
aug = np.loadtxt('8/result_norm')
sep = np.loadtxt('9/result_norm')
octo = np.loadtxt('10/result_norm')
nov = np.loadtxt('11/result_norm')
dec = np.loadtxt('12/result_norm')

plt.figure(figsize=(8,11), dpi=80)
#plt.plot(jan[:,0],jan[:,1],color='red',ls='-')

#############################################################################################
gs1 = gridspec.GridSpec(12, 1)
gs1.update(left=0.08, right=0.98, top=0.95, bottom=0.05, hspace=0.05)
ax1 = plt.subplot(gs1[0, 0])
ax2 = plt.subplot(gs1[1, 0])
ax3 = plt.subplot(gs1[2, 0])
ax4 = plt.subplot(gs1[3, 0])
ax5 = plt.subplot(gs1[4, 0])
ax6 = plt.subplot(gs1[5, 0])
ax7 = plt.subplot(gs1[6, 0])
ax8 = plt.subplot(gs1[7, 0])
ax9 = plt.subplot(gs1[8, 0])
ax10 = plt.subplot(gs1[9, 0])
ax11 = plt.subplot(gs1[10, 0])
ax12 = plt.subplot(gs1[11, 0])

#ax1.set_title('10cm')
ax1.text(0.98, 0.65, 'Jan.',horizontalalignment='right',verticalalignment='bottom',transform=ax1.transAxes,fontsize=10)
ax1.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax1.set_xticklabels([])
#ax1.set_ylabel('PA (deg)',labelpad=0)
ax1.set_ylim(0,85)
ax1.set_yticks([10,40,70])
#ax1.set_xlim(-0.2,0.2)
ax1.plot(jan[:,0],jan[:,1],color='red',ls='-')
#ax1.plot(x,s,'r-')

ax2.text(0.98, 0.65, 'Fab.',horizontalalignment='right',verticalalignment='bottom',transform=ax2.transAxes,fontsize=10)
ax2.set_ylim(0,200)
ax2.set_yticks([50,100,150])
ax2.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax2.set_xticklabels([])
ax2.plot(fab[:,0],fab[:,1],color='red',ls='-')

ax3.text(0.98, 0.65, 'Mar.',horizontalalignment='right',verticalalignment='bottom',transform=ax3.transAxes,fontsize=10)
ax3.set_ylim(0,70)
ax3.set_yticks([10,30,50])
ax3.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax3.set_xticklabels([])
ax3.plot(mar[:,0],mar[:,1],color='red',ls='-')

ax4.text(0.98, 0.65, 'Apr.',horizontalalignment='right',verticalalignment='bottom',transform=ax4.transAxes,fontsize=10)
ax4.set_ylim(0,50)
ax4.set_yticks([5,25,45])
ax4.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax4.set_xticklabels([])
ax4.plot(apr[:,0],apr[:,1],color='red',ls='-')

ax5.text(0.98, 0.65, 'May.',horizontalalignment='right',verticalalignment='bottom',transform=ax5.transAxes,fontsize=10)
ax5.set_ylim(0,65)
ax5.set_yticks([10,30,50])
ax5.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax5.set_xticklabels([])
ax5.plot(may[:,0],may[:,1],color='red',ls='-')

ax6.text(0.98, 0.65, 'Jun.',horizontalalignment='right',verticalalignment='bottom',transform=ax6.transAxes,fontsize=10)
ax6.set_ylim(0,50)
ax6.set_yticks([5,25,45])
ax6.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax6.set_xticklabels([])
ax6.plot(jun[:,0],jun[:,1],color='red',ls='-')

ax7.text(0.98, 0.65, 'Jul.',horizontalalignment='right',verticalalignment='bottom',transform=ax7.transAxes,fontsize=10)
ax7.set_ylim(0,15)
ax7.set_yticks([5,10])
ax7.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax7.set_xticklabels([])
ax7.plot(jul[:,0],jul[:,1],color='red',ls='-')

ax8.text(0.98, 0.65, 'Aug.',horizontalalignment='right',verticalalignment='bottom',transform=ax8.transAxes,fontsize=10)
ax8.set_ylim(0,55)
ax8.set_yticks([5,25,45])
ax8.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax8.set_xticklabels([])
ax8.plot(aug[:,0],aug[:,1],color='red',ls='-')

ax9.text(0.98, 0.65, 'Sep.',horizontalalignment='right',verticalalignment='bottom',transform=ax9.transAxes,fontsize=10)
ax9.set_ylim(0,55)
ax9.set_yticks([5,25,45])
ax9.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax9.set_xticklabels([])
ax9.plot(sep[:,0],sep[:,1],color='red',ls='-')

ax10.text(0.98, 0.65, 'Oct.',horizontalalignment='right',verticalalignment='bottom',transform=ax10.transAxes,fontsize=10)
ax10.set_ylim(0,390)
ax10.set_yticks([100,200,300])
ax10.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax10.set_xticklabels([])
ax10.plot(octo[:,0],octo[:,1],color='red',ls='-')

ax11.text(0.98, 0.65, 'Nov.',horizontalalignment='right',verticalalignment='bottom',transform=ax11.transAxes,fontsize=10)
ax11.set_ylim(0,60)
ax11.set_yticks([10,30,50])
ax11.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax11.set_xticklabels([])
ax11.plot(nov[:,0],nov[:,1],color='red',ls='-')

ax12.text(0.98, 0.65, 'Dec.',horizontalalignment='right',verticalalignment='bottom',transform=ax12.transAxes,fontsize=10)
ax12.set_ylim(0,56)
ax12.set_yticks([10,30,50])
ax12.set_xticks([0.5,1.5,2.5,3.5,4.5,5.5,6.5])
ax12.set_xticklabels([1,2,3,4,5,6,7])
ax12.plot(dec[:,0],dec[:,1],color='red',ls='-')
#############################################################################################

#plt.savefig("test.ps",dpi=200)

plt.show()




