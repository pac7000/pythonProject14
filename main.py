import pandas as pd
import csv
import numpy as np
from scipy.stats import gumbel_r
import matplotlib.pyplot as plt

# Replace 'book1.xlsx' with the path to your Excel file.
excel_file = 'Book1.xlsx'

# Read the first sheet with rain data
df_rain = pd.read_excel(excel_file, sheet_name='Sheet1', engine='openpyxl')

# Read the second sheet with temperature data
df_temperature = pd.read_excel(excel_file, sheet_name='Sheet2', engine='openpyxl')

# Print the dataframes to see the data (optional)
print("Rain Data:")
print(df_rain)

print("\nTemperature Data:")
print(df_temperature)

total= 55

with  open ('coyhaique.csv', 'w') as file:

    for b in range (55):

        for a in range (12):

            file.write(str(df_rain.iat[total-b,0]) + ". " + str(a+1) + ". " + str(df_rain.iat[total-b,a+1]) + " " + str(df_temperature.iat[total-b,a+1]) + '\n')


stats = df_rain.describe(include='all')
print(stats)

params = gumbel_r.fit(df_rain['january'])
print("parameters are")
print(params)

sorted_data = np.sort(df_rain['january'])
cdf = np.arange(1, len(sorted_data) + 1) / len(sorted_data)

plt.plot(sorted_data, cdf)
plt.xlabel('Data')
plt.ylabel('Cumulative Probability')
plt.title('CDF of Adjusted Data to Gumbel Distribution')
plt.grid(True)
plt.show()