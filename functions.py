#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 00:17:01 2023

@author: mac
"""
import pandas as pd
import matplotlib.pyplot as plt

def read_data_from_csv_file(filename):
    """ Function to read data from CSV file.
        Remove duplicate rows and rows conatining NAN values. Arguments:
        "filename": pass a file name/path to read data from csv file
    """
    df = pd.read_csv(filename)

    # remove invalid rows
    df.dropna(inplace=True)

    return df

def lineplot(df, figure_size=None, x_label="x", y_label="y", title=''):
    """ Function to create a lineplot. Arguments:
        A dataframe with a column "x" and other columns to be taken as y.
        Optional "figure_size" argument to change the sixe of plot.
        Optional "x_label" argument having default value of "x",
        to customise the label of x-axis.
        Optional "y_label" argument, having default value of "y",
        to customise the label of y-axis
        A list containing the headers of the columns to plot.
        It can be a source of hard to find errors.
    """

    if (figure_size is None):
        plt.figure()
    else:
        plt.figure(figsize=figure_size)

    for index, row in df.iterrows():
        plt.plot(list(df.columns[4:]), row[4:].astype(float), label=row['Series Name'])

    # labelling
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.legend()
    # save as png
    plt.savefig(title+".png")
    plt.show()
    return


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