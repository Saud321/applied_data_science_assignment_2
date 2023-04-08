import pandas as pd
import matplotlib.pyplot as plt
import functions

data = functions.read_data_from_csv_file('world_bank_data_indicators.csv')


forest_data = data[data['Series Name'] == 'Forest area (% of land area)']

# Define countries of interest and desired years
countries = ['China', 'Germany', 'India', 'Indonesia',
             'Japan', 'Russian Federation', 'United States']

forest_data = forest_data[forest_data['Country Name'].isin(countries)]

# Pivot the data to have the years as columns
forest_data_pivot = pd.pivot_table(forest_data,
                                   values=['1990', '1995', '2000',
                                           '2005', '2010', '2015'],
                                   index='Country Name')

# Plot the data
forest_data_pivot.T.plot(kind='line')
plt.xlabel('Year')
plt.ylabel('Forest area (% of land area)')
plt.title('Forest area from 1990 to 2015')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')

plt.show()
