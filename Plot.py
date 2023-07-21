# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 11:00:55 2020

@author: Viraldi
"""

from WL import *
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np

'''

Plot Matplotlib Data Well Logging

'''
def total_plot():
    
    
    
    fig, ax = plt.subplots(nrows = 1, ncols = 3, 
                            figsize=(13,20), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    fig.suptitle('Well Logging Kelompok 7', fontsize=30, 
                  y = 0.93)
    ax[0].initvert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    ax01 = ax[0].twiny() # Gamma Ray
    ax01.plot(GR, y, '-g')
    ax01.set_xlim(0,150)
    ax01.set_xlabel('Gamma Ray (GAPI)', color='g')
    ax01.tick_params(axis = 'x', colors = 'g')
    ax01.spines['top'].set_position(('outward', 12))
    
    ax02 = ax[0].twiny() # Caliper
    ax02.plot(CAL, y, '-b')
    ax02.set_xlim(6,16)
    ax02.set_xlabel('Calliper(Inch)', color='b')
    ax02.tick_params(axis = 'x', colors = 'b')
    ax02.spines['top'].set_position(('outward', 48))
    
    ax03 = ax[0].twiny() # SP
    ax03.plot(SP, y, '-r')
    ax03.plot(spb, y, '--r') #Baseline
    ax03.set_xlim(-80,20)
    ax03.set_xlabel('SP (MV)', color='r')
    ax03.tick_params(axis = 'x', colors = 'r')
    ax03.spines['top'].set_position(('outward', 88))
    
    ax04 = ax[0].twiny() # Bit Size
    ax04.plot(BS, y, '--k')
    ax04.set_xlim(6,16)
    ax04.set_xlabel('BS (Inch)', color='black')
    ax04.tick_params(axis = 'x', colors = 'black')
    ax04.spines['top'].set_position(('outward', 128))
    
    # track 2
    ax[1].grid(True, which = "both")
    ax[1].set_xlabel("Grid")
        
    ax11 = ax[1].twiny() #MSFL
    ax11.set_xlim(0.2,2000)
    ax11.semilogx(MSFL, y, color = 'black')
    ax11.set_xscale('log')
    ax11.set_xlabel('Micro SFL Resistivity(OHMM)', color='black')
    ax11.tick_params(axis = 'x', colors = 'black')
    ax11.spines['top'].set_position (('outward', 48))
    
    ax12 = ax[1].twiny() #LLS
    ax12.set_xlim(0.2,2000)
    ax12.semilogx(LLS, y, '--b')
    ax12.set_xscale('log')
    ax12.set_xlabel('Laterlog Shallow Resistivity(OHMM)', color='b')
    ax12.tick_params(axis = 'x', colors = 'b')
    ax12.spines['top'].set_position(('outward', 12))
    ax12.grid(True, which = "both")
        
    ax13 = ax[1].twiny() #LLD
    ax13.set_xlim(0.2,2000)
    ax13.semilogx(LLD, y, 'r')
    ax13.set_xscale('log')
    ax13.set_xlabel('Laterlog Deep Resistivity (OHMM)', color='r')
    ax13.tick_params(axis = 'x', colors = 'r')
    ax13.spines['top'].set_position(('outward', 88))

    #track 3
    ax[2].grid(True, which = "both")
    ax[2].set_xlabel("Grid")
    
    ax31 = ax[2].twiny() #DT
    ax31.plot(DT, y, 'b')
    ax31.set_xlim(140,40)
    ax31.set_xlabel('Delta-T(US/F)', color='b')
    ax31.tick_params(axis = 'x', colors = 'b')
    ax31.spines['top'].set_position(('outward', 12))
    
    ax32 = ax[2].twiny() #NPHI
    ax32.plot(NPHI, y, '--g')
    ax32.set_xlim(0.6,0)
    ax32.set_xlabel('Neutron Porosity(V/V)', color='g')
    ax32.tick_params(axis = 'x', colors = 'g')
    ax32.spines['top'].set_position(('outward', 48))
    
    ax33 = ax[2].twiny() #RHOB
    ax33.plot(RHOB, y, '--r')
    ax33.set_xlim(1.7,2.7)
    ax33.set_xlabel('Bulk Density RHOB (G/C3)', color='r')
    ax33.tick_params(axis = 'x', colors = 'r')
    ax33.spines['top'].set_position(('outward', 88))

'''

Plot Gamma Ray Section-1

'''

def gr_plot():
     fig, ax = plt.subplots(nrows = 1, ncols = 2, 
                            figsize=(13,20), sharey=True)
     fig.subplots_adjust(top=0.80, wspace=0.1)
     fig.suptitle('Facies from GR', fontsize=30, 
                  y = 0.93)
     ax[0].invert_yaxis()
     
     #track 1
     ax[0].grid(True, which = "both")
     ax[0].set_ylabel("Depth (m)")
     ax[0].set_xlabel("Grid")
     
     ax01 = ax[0].twiny() # Gamma Ray
     ax01.plot(GR, y, '-k', label = 'Gamma Ray')
     # ax01.plot(grb_min, y, '--b', label = 'GR Min')
     # ax01.plot(grb_max, y, '--r', label = 'GR max')
     # grb2_min = np.zeros(len(GR))
     # grb2_min[:] = np.min(GR)
     # grb2_max = np.zeros(len(GR))
     # grb2_max[:] = np.max(GR)
     
     # grb2 = grb2_max-grb2_min
     
     ax01.plot(grb_min, y, '--b', label = 'GR Min')
     ax01.plot(grb_max, y, '--r', label = 'GR max')
     ax01.plot(grbmed, y, '--c', label = 'GR med')
     # ax01.plot(grb2, y, '--g', label = 'Mid')
     

     ax01.legend()
     ax01.set_xlim(0,150)
     ax01.set_xlabel('Gamma Ray (GAPI)', color='k')
     ax01.tick_params(axis = 'x', colors = 'k')
     ax01.spines['top'].set_position(('outward', 12))
     
     #track 2
     GR_F = np.vstack((gr_facies, gr_facies)).T
     ax[1].set_xlabel('Facies')
     # cmap = mpl.colors.ListedColormap(['r', 'g', 'b'])
     ax[1].imshow(GR_F, aspect = 'auto', extent = [0, 1, max(y), min(y)])
     style = dict(size=10, color='gray')
     ax[1].text(1.05, np.min(y1)+0.8, "Shale")
     ax[1].text(1.05, np.min(y1)+2.5, "Shaly Sandstone")
     ax[1].text(1.05, np.min(y1)+9.7, "More Shaly Sandstone")
     
'''

Plot Calliper Section-2

'''
def cal_plot():
    fig, ax = plt.subplots(nrows = 1, ncols = 2, 
                            figsize=(13,20), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    fig.suptitle('Calliper Interpretation', fontsize=30, 
                  y = 0.93)
    ax[0].invert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    ax02 = ax[0].twiny() # Caliper
    ax02.plot(CAL, y, '-b')
    ax02.set_xlim(6,16)
    ax02.set_xlabel('Calliper(Inch)', color='b')
    ax02.tick_params(axis = 'x', colors = 'b')
    ax02.spines['top'].set_position(('outward', 12))
    
    ax04 = ax[0].twiny() # Bit Size
    ax04.plot(BS, y, '--k')
    ax04.set_xlim(6,16)
    ax04.set_xlabel('BS (Inch)', color='black')
    ax04.tick_params(axis = 'x', colors = 'black')
    ax04.spines['top'].set_position(('outward', 58))
    
    #track 2
    F_CAL = np.vstack((cal_facies, cal_facies)).T
    ax[1].set_xlabel('Facies')
    # cmap = mpl.colors.ListedColormap(['r', 'g', 'b'])
    ax[1].imshow(F_CAL, aspect = 'auto', extent = [0, 1, max(y), min(y)])
    ax[1].text(0.42, np.min(y1)+2.4, "Impermeable", color = "White")
    ax[1].text(0.42, np.min(y1)+30, "Impermeable", color = "White")
    ax[1].text(0.42, np.min(y1)+54, "Impermeable", color = "White")
    ax[1].text(0.42, np.min(y1)+9, "Permeable", color ="Black")
    ax[1].text(0.42, np.min(y1)+45, "Permeable", color ="Black")
    ax[1].text(0.42, np.min(y1)+64, "Permeable", color ="Black")


def tri_first_plot():
    fig, ax = plt.subplots(nrows = 1, ncols = 2, 
                            figsize=(13,20), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    fig.suptitle('Facies from SP', fontsize=30, 
                  y = 0.93)
    ax[0].invert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    
    ax01 = ax[0].twiny() # Gamma Ray
    ax01.plot(GR, y, '-k', label = 'Gamma Ray')
    ax01.plot(grb_min, y, '--b', label = 'GR Min')
    ax01.plot(grb_max, y, '--r', label = 'GR max')
    ax01.legend()
    ax01.set_xlim(0,150)
    ax01.set_xlabel('Gamma Ray (GAPI)', color='k')
    ax01.tick_params(axis = 'x', colors = 'k')
    ax01.spines['top'].set_position(('outward', 12))
    
    ax02 = ax[0].twiny() # Caliper
    ax02.plot(CAL, y, '-b', label = 'CAL')
    ax02.plot(BS, y, '-g', label = 'BS')
    ax02.set_xlim(6,16)
    ax02.legend(loc = 'upper right')
    ax02.set_xlabel('Calliper(Inch)', color='b')
    ax02.tick_params(axis = 'x', colors = 'b')
    ax02.spines['top'].set_position(('outward', 48))
    
    ax03 = ax[0].twiny() # SP
    ax03.plot(SP, y, '-y', label = 'SP')
    ax03.plot(spb, y, '--m', label = 'SP Baseline') #Baseline

    ax03.set_xlim(-80,20)
    ax03.legend(loc = 10)
    ax03.set_xlabel('SP (MV)', color='y')
    ax03.tick_params(axis = 'x', colors = 'y')
    ax03.spines['top'].set_position(('outward', 88))
    
    #track 2
    TP_F = np.vstack((tp_facies, tp_facies)).T
    ax[1].set_xlabel('Facies')
    cmap = mpl.colors.ListedColormap(['darkmagenta', 'crimson', 'gold'])
    ax[1].imshow(TP_F, aspect = 'auto', extent = [0, 1, max(y), min(y)], cmap = cmap)
    style = dict(size=10, color='gray')

def sw():
    fig, ax = plt.subplots(nrows = 1, ncols = 3, 
                            figsize=(6,20), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    # fig.suptitle('', fontsize=30, 
                  # y = 0.93)
    ax[0].invert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    ax01 = ax[0].twiny()
    ax01.plot(Sw, y1)
    ax01.set_xlim(0,1)
    ax01.set_xlabel('Water Saturation %')
    
    #track 2
    ax[1].grid(True, which = "both")
    ax[1].set_xlabel("Grid")
    
    ax02 = ax[1].twiny()
    ax02.set_xlim(np.min(Por), np.max(Por))
    ax02.plot(Por, y1, 'r')
    ax02.set_xlabel('Porosity Density')
    
    #track 3
    ax[2].grid(True, which = "both")
    ax[2].set_xlabel("Grid")
    
    ax03 = ax[2].twiny()
    ax03.set_xlim(np.min(Ps), np.max(Ps))
    ax03.plot(Ps, y1, 'g')
    ax03.set_xlabel('Porosity Sonic')

def sw():
    fig, ax = plt.subplots(nrows = 1, ncols = 3, 
                            figsize=(6,20), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    # fig.suptitle('', fontsize=30, 
                  # y = 0.93)
    ax[0].invert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    ax01 = ax[0].twiny()
    ax01.plot(Sw, y1)
    ax01.set_xlim(0,1)
    ax01.set_xlabel('Water Saturation %')
    
    #track 2
    ax[1].grid(True, which = "both")
    ax[1].set_xlabel("Grid")
    
    ax02 = ax[1].twiny()
    ax02.set_xlim(np.min(Por), np.max(Por))
    ax02.plot(Por, y1, 'r')
    ax02.set_xlabel('Porosity Density')
    
    #track 3
    ax[2].grid(True, which = "both")
    ax[2].set_xlabel("Grid")
    
    ax03 = ax[2].twiny()
    ax03.set_xlim(np.min(Ps), np.max(Ps))
    ax03.plot(Ps, y1, 'g')
    ax03.set_xlabel('Porosity Sonic')


def resis_week2_plot():
    fig, ax = plt.subplots(nrows = 1, ncols = 4, 
                            figsize=(13,20), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    # fig.suptitle('', fontsize=30, 
                  # y = 0.93)
    ax[0].invert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    
    ax01 = ax[0].twiny() # Gamma Ray
    ax01.plot(GR, y, '-k', label = 'Gamma Ray')
    ax01.plot(grb_min, y, '--b', label = 'GR Min')
    ax01.plot(grb_max, y, '--r', label = 'GR max')
    ax01.legend()
    ax01.set_xlim(0,150)
    ax01.set_xlabel('Gamma Ray (GAPI)', color='k')
    ax01.tick_params(axis = 'x', colors = 'k')
    ax01.spines['top'].set_position(('outward', 12))
    
    ax02 = ax[0].twiny() # Caliper
    ax02.plot(CAL, y, '-b', label = 'CAL')
    ax02.plot(BS, y, '-g', label = 'BS')
    ax02.set_xlim(6,16)
    ax02.legend(loc = 'upper right')
    ax02.set_xlabel('Calliper(Inch)', color='b')
    ax02.tick_params(axis = 'x', colors = 'b')
    ax02.spines['top'].set_position(('outward', 48))
    
    ax03 = ax[0].twiny() # SP
    ax03.plot(SP, y, '-y', label = 'SP')
    ax03.plot(spb, y, '--m', label = 'SP Baseline') #Baseline

    ax03.set_xlim(-80,20)
    ax03.legend(loc = 10)
    ax03.set_xlabel('SP (MV)', color='y')
    ax03.tick_params(axis = 'x', colors = 'y')
    ax03.spines['top'].set_position(('outward', 88))
    
    #track 2
    TP_F = np.vstack((tp_facies, tp_facies)).T
    ax[1].set_xlabel('Facies')
    cmap = mpl.colors.ListedColormap(['darkmagenta', 'crimson', 'gold'])
    ax[1].imshow(TP_F, aspect = 'auto', extent = [0, 1, max(y), min(y)], cmap = cmap)
    style = dict(size=10, color='gray')
    
    #Track 3
    ax[2].grid(True, which = "both")
    ax[2].set_xlabel("Grid")
        
    ax11 = ax[2].twiny() #MSFL
    ax11.set_xlim(0.2,2000)
    ax11.semilogx(MSFL, y, color = 'black')
    ax11.set_xscale('log')
    ax11.set_xlabel('Micro SFL Resistivity(OHMM)', color='black')
    ax11.tick_params(axis = 'x', colors = 'black')
    ax11.spines['top'].set_position (('outward', 48))
    
    ax12 = ax[2].twiny() #LLS
    ax12.set_xlim(0.2,2000)
    ax12.semilogx(LLS, y, '--b')
    ax12.set_xscale('log')
    ax12.set_xlabel('Laterlog Shallow Resistivity(OHMM)', color='b')
    ax12.tick_params(axis = 'x', colors = 'b')
    ax12.spines['top'].set_position(('outward', 12))
    ax12.grid(True, which = "both")
        
    ax13 = ax[2].twiny() #LLD
    ax13.set_xlim(0.2,2000)
    ax13.semilogx(LLD, y, 'r')
    ax13.set_xscale('log')
    ax13.set_xlabel('Laterlog Deep Resistivity (OHMM)', color='r')
    ax13.tick_params(axis = 'x', colors = 'r')
    ax13.spines['top'].set_position(('outward', 88))
    
    #track 4
    RES_F = np.vstack((res_facies, res_facies)).T
    ax[3].set_xlabel('Fluid Content')
    cmap = mpl.colors.ListedColormap(['red', 'black', 'blue', 'white'])
    ax[3].imshow(RES_F, aspect = 'auto', extent = [0, 1, max(y), min(y)], cmap = cmap)
    style = dict(size=10, color='gray')
    
    
def quali_week_3():
    fig, ax = plt.subplots(nrows = 1, ncols = 5, 
                            figsize=(16,25), sharey=True)
    fig.subplots_adjust(top=0.80, wspace=0.1)
    
    ax[0].invert_yaxis()
    
    #track 1
    ax[0].grid(True, which = "both")
    ax[0].set_ylabel("Depth (m)")
    ax[0].set_xlabel("Grid")
    
    
    ax01 = ax[0].twiny() # Gamma Ray
    ax01.plot(GR, y, '-k', label = 'Gamma Ray')
    ax01.plot(grb_min, y, '--b', label = 'GR Min')
    ax01.plot(grb_max, y, '--r', label = 'GR max')
    ax01.legend()
    ax01.set_xlim(0,150)
    ax01.set_xlabel('Gamma Ray (GAPI)', color='k')
    ax01.tick_params(axis = 'x', colors = 'k')
    ax01.spines['top'].set_position(('outward', 12))
    
    ax02 = ax[0].twiny() # Caliper
    ax02.plot(CAL, y, '-b', label = 'CAL')
    ax02.plot(BS, y, '-g', label = 'BS')
    ax02.set_xlim(6,16)
    ax02.legend(loc = 'upper right')
    ax02.set_xlabel('Calliper(Inch)', color='b')
    ax02.tick_params(axis = 'x', colors = 'b')
    ax02.spines['top'].set_position(('outward', 48))
    
    ax03 = ax[0].twiny() # SP
    ax03.plot(SP, y, '-y', label = 'SP')
    ax03.plot(spb, y, '--m', label = 'SP Baseline') #Baseline

    ax03.set_xlim(-80,20)
    ax03.legend(loc = 10)
    ax03.set_xlabel('SP (MV)', color='y')
    ax03.tick_params(axis = 'x', colors = 'y')
    ax03.spines['top'].set_position(('outward', 88))
    
    #track 2
    TP_F = np.vstack((tp_facies, tp_facies)).T
    ax[3].set_xlabel('Facies')
    cmap = mpl.colors.ListedColormap(['darkmagenta', 'crimson', 'gold'])
    ax[3].imshow(TP_F, aspect = 'auto', extent = [0, 1, max(y), min(y)], cmap = cmap)
    style = dict(size=10, color='gray')
    
    #Track 3
    ax[3].grid(True, which = "both")
    ax[3].set_xlabel("Grid")
        
    ax11 = ax[1].twiny() #MSFL
    ax11.set_xlim(0.2,2000)
    ax11.semilogx(MSFL, y, color = 'black')
    ax11.set_xscale('log')
    ax11.set_xlabel('Micro SFL Resistivity(OHMM)', color='black')
    ax11.tick_params(axis = 'x', colors = 'black')
    ax11.spines['top'].set_position (('outward', 48))
    
    ax12 = ax[1].twiny() #LLS
    ax12.set_xlim(0.2,2000)
    ax12.semilogx(LLS, y, '--b')
    ax12.set_xscale('log')
    ax12.set_xlabel('Laterlog Shallow Resistivity(OHMM)', color='b')
    ax12.tick_params(axis = 'x', colors = 'b')
    ax12.spines['top'].set_position(('outward', 12))
    ax12.grid(True, which = "both")
        
    ax13 = ax[1].twiny() #LLD
    ax13.set_xlim(0.2,2000)
    ax13.semilogx(LLD, y, 'r')
    ax13.set_xscale('log')
    ax13.set_xlabel('Laterlog Deep Resistivity (OHMM)', color='r')
    ax13.tick_params(axis = 'x', colors = 'r')
    ax13.spines['top'].set_position(('outward', 88))
    
    #track 4
    RES_F = np.vstack((res_facies, res_facies)).T
    ax[4].set_xlabel('Fluid Content')
    cmap = mpl.colors.ListedColormap(['red', 'black', 'blue', 'white'])
    # cmap = mpl.colors.ListedColormap(['white'])
    ax[4].imshow(RES_F, aspect = 'auto', extent = [0, 1, max(y), min(y)], cmap = cmap)
    style = dict(size=10, color='gray')
    
    #track 5
    ax[2].grid(True, which = "both")
    ax[2].set_xlabel("Grid")
    
    ax32 = ax[2].twiny() #NPHI
    ax32.plot(NPHI, y, '--g')
    ax32.set_xlim(0.6,0)
    ax32.set_xlabel('Neutron Porosity(V/V)', color='g')
    ax32.tick_params(axis = 'x', colors = 'g')
    ax32.spines['top'].set_position(('outward', 48))
    
    ax33 = ax[2].twiny() #RHOB
    ax33.plot(RHOB, y, '--r')
    ax33.set_xlim(1.7,3)
    ax33.set_xlabel('Bulk Density RHOB (G/C3)', color='r')
    ax33.tick_params(axis = 'x', colors = 'r')
    ax33.spines['top'].set_position(('outward', 88))

def prog3_1():
    pickett_figure = plt.figure(figsize = (7,6))
    plt.loglog(df1.NPHI, df1.RHOB, 'ro', label = '', color = 'red')
    plt.ylim(3,1.8)
    plt.xlim(-5, 44.4)
    plt.ylabel('Bulk Density [g/cm3]')
    plt.xlabel('Neutron Porosity NPHI [V/V]')
    # ax.grid(True, which = "both")
    
def prog3_2():
    pickett_figure = plt.figure(figsize = (7,6))
    plt.loglog(Ps, df1.RHOB, 'ro', label = '', color = 'red')
    plt.ylim(3,1.8)
    # plt.xlim(40, 130)
    plt.ylabel('Bulk Density [g/cm3]')
    plt.xlabel('Porosity Sonic [usec/ft]')
    # ax.grid(True, which = "both")
     
    