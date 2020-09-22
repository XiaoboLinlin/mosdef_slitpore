import scipy as sp
import numpy as np
import matplotlib.pyplot as plt
import csv as csv
import pandas as pd
import itertools as it
from collections import defaultdict
import os
import shutil
import matplotlib as matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.axis as axis
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d
from scipy.signal import savgol_filter
import math
from matplotlib import rcParams
rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']
import pylab as plot

#********************************
#Notes
#********************************

#Plots 2 item:
#1) a pairwise energy for indiviual peeling strands, and non-peeling strands
#2)
#********************************
#End Notes
#********************************
# only change the below reading_file
E_vs_P_Psat_saving_name = "GOMC_E_vs_P_Psat_gomc.pdf"

axis_Label_font_size = 24
legend_font_size = 18
axis_number_font_size = 20

PointSizes = 8
ConnectionLineSizes = 2
Reg_Density_Linestyle = '--'  #'-' =  solid, '--' = dashed, ':'= dotted
Critical_Density_Linestyle = None


#**************
# P vs T plot ranges (start)
#*************
Psat_min = 0.001
Psat_max = 15



E_min = 0.001
E_max = 25

E_ticks_major = 5
E_ticks_minor = 1

#**************
# P vs T plot ranges (end)
#*************

Chemical_name = 'grapene_water'


Color_for_Plot_10A_slit =  'b'  #gray
Color_for_Plot_16A_slit =  'r'  #gray




#********************************
#  File importing 
#********************************

calc_data_reading_name_10A_ads = '../adsorption/3x3x1.0nm_3-layer/gomc/analysis/adsorption_10A_slit_df.txt'
calc_data_reading_name_16A_ads = '../adsorption/3x3x1.6nm_3-layer/gomc/analysis/adsorption_16A_slit_df.txt'

calc_data_reading_name_10A_des = '../desorption/3x3x1.0nm_3-layer/gomc/analysis/desorption_10A_slit_df.txt'
calc_data_reading_name_16A_des = '../desorption/3x3x1.6nm_3-layer/gomc/analysis/desorption_16A_slit_df.txt'

calc_data_10A_ads = pd.read_csv(calc_data_reading_name_10A_ads,  sep='\s+', index_col=0)
calc_data_10A_ads_df = pd.DataFrame(calc_data_10A_ads)

calc_data_16A_ads = pd.read_csv(calc_data_reading_name_16A_ads,  sep='\s+', index_col=0)
calc_data_16A_ads_df = pd.DataFrame(calc_data_16A_ads)

calc_data_10A_des = pd.read_csv(calc_data_reading_name_10A_des,  sep='\s+', index_col=0)
calc_data_10A_des_df = pd.DataFrame(calc_data_10A_des)

calc_data_16A_des = pd.read_csv(calc_data_reading_name_16A_des,  sep='\s+', index_col=0)
calc_data_16A_des_df = pd.DataFrame(calc_data_16A_des)

Psat_ratio_10A_ads = calc_data_10A_ads_df.loc[:, 'Psat_ratio' ].tolist()
Psat_ratio_16A_ads = calc_data_16A_ads_df.loc[:, 'Psat_ratio' ].tolist()
Psat_ratio_10A_des = calc_data_10A_des_df.loc[:, 'Psat_ratio' ].tolist()
Psat_ratio_16A_des = calc_data_16A_des_df.loc[:, 'Psat_ratio' ].tolist()


Avg_E_No_water_per_nm_sq_10A_ads= calc_data_10A_ads_df.loc[:, 'Avg_E_No_water_per_nm_sq' ].tolist()
Avg_E_No_water_per_nm_sq_16A_ads= calc_data_16A_ads_df.loc[:, 'Avg_E_No_water_per_nm_sq' ].tolist()
Avg_E_No_water_per_nm_sq_10A_des= calc_data_10A_des_df.loc[:, 'Avg_E_No_water_per_nm_sq' ].tolist()
Avg_E_No_water_per_nm_sq_16A_des= calc_data_16A_des_df.loc[:, 'Avg_E_No_water_per_nm_sq' ].tolist()

StdDev_E_No_water_per_nm_sq_10A_ads= calc_data_10A_ads_df.loc[:, 'StdDev_E_No_water_per_nm_sq' ].tolist()
StdDev_E_No_water_per_nm_sq_16A_ads= calc_data_16A_ads_df.loc[:, 'StdDev_E_No_water_per_nm_sq' ].tolist()
StdDev_E_No_water_per_nm_sq_10A_des= calc_data_10A_des_df.loc[:, 'StdDev_E_No_water_per_nm_sq' ].tolist()
StdDev_E_No_water_per_nm_sq_16A_des= calc_data_16A_des_df.loc[:, 'StdDev_E_No_water_per_nm_sq' ].tolist()


#********************************
#  End File importing for Final States
#********************************



# ********************************
#  End File importing
# ********************************




#****************************************
#Plot Number 2  (P vs T) (start)
#****************************************

# Plotting curve data below

fig1 = plt.figure()
ax1 = fig1.add_subplot(1, 1, 1)
#ax2 = ax1.twiny()

for tick in ax1.xaxis.get_ticklabels():
    tick.set_fontname('Arial')
for tick in ax1.yaxis.get_ticklabels():
    tick.set_fontname('Arial')

plt.xlabel('$P/P_{sat}$', fontname="Arial", fontsize=axis_Label_font_size)
plt.ylabel('$\u03BE$ (waters/$nm^2$)', fontname="Arial", fontsize=axis_Label_font_size)


# Matplotlib colors b : blue, g : green, r : red, c : cyan, m : magenta, y : yellow, k : black, w : white, gray='x' (x=0 to 1)
plt.plot(Psat_ratio_10A_ads, Avg_E_No_water_per_nm_sq_10A_ads , color='b', marker='D', linestyle='-' , markersize=PointSizes, linewidth=ConnectionLineSizes, fillstyle='full', label= "10 $\AA$ ads") #label=File_label_No1
plt.plot(Psat_ratio_16A_ads, Avg_E_No_water_per_nm_sq_16A_ads , color='r', marker='o', linestyle='-' , markersize=PointSizes, linewidth=ConnectionLineSizes, fillstyle='full', label= "16 $\AA$ ads") #label=File_label_No1

plt.plot(Psat_ratio_10A_des, Avg_E_No_water_per_nm_sq_10A_des , color='b', marker='D', linestyle='--' , markersize=PointSizes, linewidth=ConnectionLineSizes, fillstyle='none', label= "10 $\AA$ des") #label=File_label_No1
plt.plot(Psat_ratio_16A_des, Avg_E_No_water_per_nm_sq_16A_des , color='r', marker='o', linestyle='--' , markersize=PointSizes, linewidth=ConnectionLineSizes, fillstyle='none', label= "16 $\AA$ des") #label=File_label_No1



#major_xticks = np.arange(Psat, Psat_max+0.001, Psat_ticks_major)
major_yticks = np.arange(E_min, E_max+0.001, E_ticks_major)

#minor_xticks = np.arange(Psat, Psat_max+0.001, Psat_ticks_minor )
minor_yticks = np.arange(E_min, E_max+0.001, E_ticks_minor)


#plt.gca().set_xlim(left=2, right=105)

#ax1.set_xticks(major_xticks)
#ax1.set_xticks(minor_xticks, minor=True)
ax1.set_yticks(major_yticks)
ax1.set_yticks(minor_yticks, minor=True)


ax1.tick_params(axis='both', which='major', length=4, width=2, labelsize=axis_number_font_size, top=True, right=True)
ax1.tick_params(axis='both', which='minor', length=4, width=1, labelsize=axis_number_font_size, top=True, right=True)



leg1 = ax1.legend(loc='upper left', shadow=True, fontsize=legend_font_size ,prop={'family':'Arial','size': legend_font_size})

plt.tight_layout()  # centers layout nice for final paper
# plt.gcf().subplots_adjust(bottom=0.15) # moves plot up so x label not cutoff
plt.xlim(Psat_min, Psat_max)  # set plot range on x axis
plt.ylim(E_min, E_max)  # set plot range on y axis

plt.gcf().subplots_adjust(left=0.25, bottom=None, right=0.90, top=None, wspace=None, hspace=None) # moves plot  so x label not cutoff

frame1 = leg1.get_frame()
frame1.set_facecolor('0.90')

plt.xscale("log")

ax1.xaxis.set_major_locator(ticker.LogLocator(base=10.0, numticks=5))
ax1.xaxis.set_minor_locator(ticker.LogLocator(base=10.0, numticks=5))

plt.grid()

plt.legend(ncol=1,loc='upper left', fontsize=legend_font_size, prop={'family':'Arial','size': legend_font_size})

plt.show()
fig1.savefig(E_vs_P_Psat_saving_name)
#****************************************
#Plot Number 1  P vs T) (end)
#****************************************

