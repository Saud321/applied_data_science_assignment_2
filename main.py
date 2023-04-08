#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def bar_graph(indicator, data, years, title, x_label='x', y_label='y'):
    """ Function to create a barplot. Arguments:
        "indicator": against whic parameter to draw a plot graph
        "data":  argument is the data frame which is used to populate th data
        in bar graph
        "years": argument is used to plot data against specific years
        "title": "Title of the bar plot",
        "x_label" argument having default value of "x",
        to customise the label of x-axis.
        "y_label" argument, having default value of "y",
        to customise the label of y-axis
    """

    # Plot bar graph
    df_bar = data[data['Series Name'].isin([indicator])]

    # create a new data frame for plotting
    df_pivot = df_bar.pivot(index='Country Code',
                            columns='Series Name', values=years)
    # Define the graph
    ax = df_pivot.plot(kind='bar', rot=0, figsize=(15, 15))

    plt.title(title, fontsize=16)
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)

    # legend labels
    handles, labels = ax.get_legend_handles_labels()
    new_labels = [label.split(',')[0][1:] for label in labels]
    plt.legend(handles, new_labels, title='Year', fontsize=14)
    plt.savefig(title+".png")
    plt.show()


def read_data_from_file(filename):

    df = pd.read_csv(filename)

    # remove invalid rows
    df.dropna(inplace=True)

    # remove duplicates
    df.drop_duplicates(inplace=True)

    return df


data = read_data_from_file('world_bank_data_indicators.csv')


indicators = ['Urban population (% of total population)',
              'CO2 emissions (metric tons per capita)',
              'CO2 emissions from liquid fuel consumption (% of total)',
              'CO2 emissions from transport (% of total fuel combustion)']

titles = ['Top 10 Countries Urban population',
          'Top 10 Countries CO2 emissions',
          'Top 10 Countries from liquid fuel consumption',
          'Top 10 Countries CO2 emissions from transport']

years = [col for col in data.columns if col.isdigit()]


for i, indicator in enumerate(indicators):
    bar_graph(indicator, data, years, titles[i], 'Country', indicator)
