#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 21:06:59 2020

@author: dipanshu
"""
import pandas as pd
import numpy as np

data = pd.read_csv('data/processed_data.csv')

parameter_grouped_data = data.groupby('parameterid')
mv_stdev = parameter_grouped_data.mv.std()
mv_mean = parameter_grouped_data.mv.mean()

for i in range(len(data)):
    data.at[i,'mean']=mv_mean[data.loc[i]['parameterid']]
    data.at[i,'standard_dev']=mv_stdev[data.loc[i]['parameterid']]
    
data.to_csv('data/data_w_mean_std.csv')

