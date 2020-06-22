#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 11:35:16 2020

@author: dipanshu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

data = pd.read_csv('data/data_w_mean_std.csv')

parameter_grouped_data = dict(list(data.groupby('parameterid')))
parameters = list(parameter_grouped_data.keys())
for index,parameter in enumerate(parameters):
    plt.figure(figsize=[12,6])
    
    mean=parameter_grouped_data[parameter]['mean'].mean()
    standard_dev=parameter_grouped_data[parameter].standard_dev.mean()
    target = parameter_grouped_data[parameter].target_value.mean()
    if(mean==target):
        target+=1
    
    if(standard_dev==0):
        print('data not enough... aborting for',parameter)
        continue
    
    usl = parameter_grouped_data[parameter].usl.mean()
    lsl = parameter_grouped_data[parameter].lsl.mean()
    
    plt.axvline(usl,linestyle='dashed',label='USL ='+str(usl),color='b')
    plt.axvline(lsl,linestyle='dashed',label='LSL ='+str(lsl),color='g')
    plt.axvline(mean,linestyle='dashed',label='mean ='+str(mean),color='red')
    plt.axvline(target,linestyle='dashed',label='target value ='+str(target),color='yellow')
    
    n,bins,patches = plt.hist(parameter_grouped_data[parameter].mv, align='mid', color=(0.4, 0.6, 0.6, 1), edgecolor='black',density=True)
    for i in range(len(bins)-1):
        bar_val = (bins[i]+bins[i+1])/2
        if(bar_val<lsl or bar_val>usl):
            patches[i].set_fc('r')
    
    bell_x = [(bins[i]+bins[i+1])/2 for i in range(len(bins)-1)]
    bell_y = n
    expected_x = np.linspace(mean-standard_dev*5,mean+standard_dev*5,1000)
    expected_y = st.norm(mean,standard_dev).pdf(expected_x)
    
    plt.plot(bell_x,bell_y,linestyle='dashed',color='black',label='lineCurve')
    plt.plot(expected_x,expected_y,color='red',label='expected bell curve')
    plt.xlim([mean-10*standard_dev,mean+10*standard_dev])
    
    plt.legend()
    plt.savefig('graphs/'+str(parameter)+'.png')
    plt.close()
    print('progress: ',round((index/len(parameters))*100,2),'graphed',parameter,'...')

print('process has completed... thank you for your patience =)')
    
    
