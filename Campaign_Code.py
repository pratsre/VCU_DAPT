# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Import Data as Dataframe
import numpy as np
from pandas import Series,DataFrame
import pandas as pd

df = pd.read_table('campaign', sep = '|', header=None)

#Rename Columns for Campaign Data
df = df.rename(columns={0 :'EID', 1 : 'Camp_Name',
                        2: 'CampaignID', 3:'CampaignType',
                        4: 'Start Date', 5: 'End Date',
                        6: 'Deactivation Date', 7:'Deactivation Reason',
                        8:'Budget Cap',9:'Application Cap'})

#Quick summary stats on integer fields
print df.describe()

#Count number of nulls in each columns
df.isnull().sum()

#Cout number of Zeroes in ID Column
(df==0).astype(int).sum()