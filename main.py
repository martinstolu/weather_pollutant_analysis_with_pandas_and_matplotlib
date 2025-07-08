import  pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


air_data = pd.read_csv('openaq.csv', sep=';')
air_data['Last Updated'] = pd.to_datetime(air_data['Last Updated'], utc=True)
air_data['Last_Updated_date'] = air_data['Last Updated'].dt.date
air_data= air_data.sort_values(by=['Last Updated'], ascending=False)
# air_data = air_data[air_data['City'].isin(['Warszawa'])]

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)



print(f"\n\n\n {air_data.head()}\n\n")

"""1. Seasonal pollution trends analysis
Identify whether pollutant levels (like PM2.5 or NO2) vary significantly by season or month in Warsaw or other cities.

Detect any patterns like winter smog peaks or summer ozone rises.

"""
air_data['YEAR'] = air_data['Last Updated'].dt.year
air_data['Month'] = air_data['Last Updated'].dt.month
difference_in_NO2PM25 = air_data[(air_data.Pollutant.isin(['O3','NO2']))]
print(difference_in_NO2PM25.head())
sns.lineplot(air_data, x='YEAR', y='Value', hue='Pollutant')
sns.set_style('dark')

plt.show()




