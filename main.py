#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import functions

data = functions.read_data_from_csv_file('world_bank_data_indicators.csv')


indicators = ['CO2 emissions (metric tons per capita)',
              'CO2 emissions from liquid fuel consumption (% of total)',
              'CO2 emissions from gaseous fuel consumption (% of total)']

titles = ['Top 10 Countries CO2 emissions',
          'Top 10 Countries CO2 emissions from liquid fuel consumption',
          'Top 10 Countries CO2 emissions from gaseous fuel consumption']

years = [col for col in data.columns if col.isdigit()]

stats = data.groupby(['Country Name', 'Series Name']).describe()

# Print the statistics
print(stats)

for i, indicator in enumerate(indicators):
    functions.bar_graph(indicator, data, years, titles[i],
                        'Country', indicator)
