#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 20:20:03 2023

@author: mac
"""


import functions

df = functions.read_data_from_csv_file('world_bank_data_indicators.csv')


# Selecting only the data for China
china_df = df[df['Country Name'] == 'China']


functions.lineplot(china_df, (20, 10), 'Year', 'Value',
                   'China - Forest area and CO2 emissions')
