#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 12:32:11 2020

@author: dipanshu
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st

data = pd.read_csv('data/data_w_mean_std.csv')

parameter_grouped_data = dict(list(data.groupby('parameterid')))
parameters = list(parameter_grouped_data.keys())

outliers = pd.DataFrame(columns=data.columns)

for parameter in parameters:
    df = parameter_grouped_data[parameter]
    mean=parameter_grouped_data[parameter]['mean'].mean()
    standard_dev=parameter_grouped_data[parameter].standard_dev.mean()
    usl = parameter_grouped_data[parameter].usl.mean()
    lsl = parameter_grouped_data[parameter].lsl.mean()
    outlier_df = df.loc[(df.mv>usl) | (df.mv<lsl)]
    outliers=pd.concat([outliers,outlier_df],ignore_index=True)
    
outliers.to_csv('data/outlier_data.csv',index=False)