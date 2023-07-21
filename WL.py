#This Code is refer to Tugas Well Logging
#Viraldi 07/09/2020

import lasio
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib as mpl
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.ticker as ticker
import Plot

# Importing Lasio 
las = lasio.read("D:/KULIAH/S1/Tugas/Semester 7/Well Logging/Python Processing/MLD-05-B1, OH 12.25Inch Combined.las")

# Making dataframe 0
df = las.df()

'''

Indexing

'''
LLD0 = df['LLD']
LLS0 = df['LLS']
DT0 = df['DT']
SP0 = df['SP']
MSFL0 = df['MSFL']
GR0 = df['GR']
NPHI0 = df['NPHI']
DRHO0 = df['DRHO']
PEF0 = df['PEF']
RHOB0 = df['RHOB']
CAL0 = df['CALI']

#Making dataframe 1
df1 = df.iloc[::-1]

#Change data index from feet to m
df1.index *= 0.3048

# Selecting Data range
df1 = df1[2496:2562] # Kelompok 7 2496-2562

# Set the Dataset
y = df1.index
y1 = df1.index.values

LLD = df1['LLD']
LLS = df1['LLS']
DT = df1['DT']
SP = df1['SP']
MSFL = df1['MSFL']
GR = df1['GR']
NPHI = df1['NPHI']
DRHO = df1['DRHO']
PEF = df1['PEF']
RHOB = df1['RHOB']
CAL = df1['CALI']

'''

Import Kuantitatif

'''
dfk = pd.read_csv('kuantia.csv', sep = ';',index_col = 'depth')
dfk = dfk.iloc[::-1]
dfk1 = dfk[2496:2562]
yk = dfk1.index.values

sw = []
sWa = ((1/(dfk1['F'].values**2))*
      (dfk1['Rw'].values/dfk1['Rt'].values))**(1/2)
sWa = sWa*100

'''
To Measure Sw
'''
# Porosity Density
Por = []
Por = (2.65 - dfk1.RHOB)/(2.65 - 1.1)
df1['Porosity Density'] = Por.values

Sw = [len(Por)]
Sw = ((df1.LLD.values/dfk1.Rw.values)*Por**2)**(-1/2)
Sw = Sw/10
df1['Water Saturation'] = Sw.values



'''
end of measure Sw
'''

# Porosity Sonic
Ps = []
Ps = (df1.DT - 55.5)/(189 - 55.5)
df1['Porosity Saturation'] = Ps.values


'''

Measurement

'''

# Bitsize
BS = np.zeros(len(GR))
BS[:] = 12.5

# Vshale Measurement
Vsh=[]
GRmin = 10 #Rio,2020 for Baturaja
GRmax = 110 #Rio,2020 for Baturaja
IGR = (GR-GRmin)/(GRmax-GRmin) #Index Gamma Ray

Vsh = 0.083*(2**(3.7*(IGR)-1))
Vsh = Vsh*100 #Persen
df1['Vshale'] = Vsh

# Fixing SP to -80_20
df1['SP'] = SP + 505


'''

Baseline

'''
# Gamma Ray Baseline
grb_min = np.zeros(len(GR))
grb_min[:] = GRmin

grb_max = np.zeros(len(GR))
grb_max[:] = GRmax

grbmed = (grb_max+grb_min)/2


# SP Baseline
spb = np.zeros(len(SP))
spb[:] = 0

# Calliper Baseline
calb = np.zeros(len(CAL))
calb[:] = BS[:]


'''

Qualitative Interpreatation

'''

#Gamma Ray


gr_top_pick = [np.min(y1)-1, 2497, 2499, 2501, 2504.5, 2506, 2510, 
               2519, 2521, 2523, 2528.5, 2529.5, 2533.8, 2535.5, 2538,
               2539.5, 2547, 2550,2554,2555.8,
               np.max(y1)]
gr_f = [1,3,1,3,3,1,1,1,1,1,1,1,1,3,2,3,1,3,1,3]

gr_label = ('Shale', 'Shaly Sand', 'Sandstone')

gr_facies = np.zeros(len(GR))

for i in range(len(y1)):
    for j in range(len(gr_top_pick)-1):
        if y1[i] > gr_top_pick[j] and y1[i] <= gr_top_pick[j+1]:
            gr_facies[i]=gr_f[j]
                

df1['FACIES'] = gr_facies


# Tri Plot
tp_top_pick = [np.min(y1)-1, 2497, 2499, 2501, 2504.5, 2506, 2516, 
               2519, 2521, 2523, 2528.5, 2529.5, 2533.8, 2535.5, 2538,
               2539.5, 2547, 2550,2554,2555.8,
               np.max(y1)]
tp_f = [1,3,1,3,2,3,1,3,2,3,2,3,1,3,2,3,2,3,2,3]

tp_label = ('reservoir', 'not interested zone')

tp_facies = np.zeros(len(GR))

for i in range(len(y1)):
    for j in range(len(tp_top_pick)-1):
        if y1[i] > tp_top_pick[j] and y1[i] <= tp_top_pick[j+1]:
            tp_facies[i]=gr_f[j]

# Res Analysis
res_top_pick = [np.min(y1)-1 ,2496.95,2497, 2497.4,2499, 
                2501, 2502.3,2503.5,2506, 2535.8, 2537, 
                2539.3,2540, 2544, 2546.7,2549,
                2550,2551.5,2551.7,2553.1,2554.8,
                2556,2557.8,2559.3,2560.1,2561,
                np.max(y1)]
res_f = [4,2,1,3,4,1,2,3,4,1,2,4,2,3,4,1,2,4,1,2,4,3,4,1,4,2]

res_label = ('reservoir', 'not interested zone')

res_facies = np.zeros(len(GR))

for i in range(len(y1)):
    for j in range(len(res_top_pick)-1):
        if y1[i] > res_top_pick[j] and y1[i] <= res_top_pick[j+1]:
            res_facies[i]=res_f[j]
            
'''
Pembagian Garis

'''
depth_pick = [2496.0072, 2505.3036, 2519.0196, 2533.0404000000003, 
              2546.1468, 2554.0716]

replacement = np.ones(len(depth_pick))

df1['Picking'] = False
df1.loc[depth_pick, 'Picking'] = True


    # ax2.axvline(x=x,ymin=0,ymax=1.2,c="red",linewidth=2, zorder=0,clip_on=False)