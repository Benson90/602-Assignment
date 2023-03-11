#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 14:26:21 2023

@author: benson
"""

import pandas as pd


weather = 'https://raw.githubusercontent.com/data602sps/datasetspractice/main/weather.csv'
salary = 'https://raw.githubusercontent.com/data602sps/datasetspractice/main/salarydata.csv'
typhoon = 'https://raw.githubusercontent.com/Benson90/602-Assignment/main/typhoon_data.csv'
unemployment = 'https://raw.githubusercontent.com/Benson90/602-Assignment/main/Unemployment%20in%20America%20Per%20US%20State.csv'


# Q1. Load your dataset into python using the pandas library and save data into a dataframe named dfi (where i is one of your datasets, for a total of 4).
df1 = pd.read_csv(weather,index_col=0)
df2 = pd.read_csv(salary)
df3 = pd.read_csv(typhoon,index_col=0)
df4 = pd.read_csv(unemployment,index_col=0)

# Q2. Preview your data by calling your dataframe’s name. How many columns and rows do you see?
df1.info()
print("8719 rows and 14 columns")
df2.info()
print("51 rows x 2 columns")
df3.info()
print("68624 rows x 17 columns")
df4.info()
print("29892 rows and 10 columns")

# Q3. Examine the shape of your data using the .shape command and the data types of your columns using .dtypes.3
print(df1.shape)
print(df1.dtypes)

print(df2.shape)
print(df2.dtypes)

print(df3.shape)
print(df3.dtypes)

print(df4.shape)
print(df4.dtypes)

# Q4. Use .describe() on your data. What do you notice about your data? What does this command return?
print(df1.describe())
print(df2.describe())
print(df3.describe())
print(df4.describe())

print("The data return in count, mean, std, min, 25%, 50%, 75% and max, and it is not return data type object")

# Q5. Use the .head() and .tail() command - what does this do?

print(df1.head())
print(df1.tail())
print(df2.head())
print(df2.tail())
print(df3.head())
print(df3.tail())
print(df4.head())
print(df4.tail())

print("It will show the first 5 row and last 5 row data")


# Extra Credit (3 pts)
# 1. Choose one of your datasets and remove the header information. (Can delete the row in excel, etc..)
# 2. Import the data into your environment using pandas. Display the .head() of your data showing no header information.

typhoon_no_header = 'https://raw.githubusercontent.com/Benson90/602-Assignment/main/typhoon_data_no_header.csv'
df_no_header = pd.read_csv(typhoon_no_header,index_col=0,header=None)
print(df_no_header.head())

# 3. Using pandas, update the dataset to include the header information. Display the updated data using .head().

col_Names=["natioanl number", "year", "month", "day", "hour", "grade", "Latitude of the center", "Longitude of the center", "Central pressure", "Maximum sustained wind speed", "Direction of the longest radius of 50kt winds or greater", "The longeast radius of 50kt winds or greater", "The shortest radius of 50kt winds or greater", "Direction of the longest radius of 30kt winds or greater", "The longeast radius of 30kt winds or greater", "The shortest radius of 30kt winds or greater", "Indicator of landfall or passage"]
df_add_header= pd.read_csv(typhoon_no_header, index_col=0, names=col_Names)
print(df_add_header.head())

# Extra Credit (3 pts)
# 1. Import a “dirty” dataset from the internet into your environment. (Missing values, improper coding of columns, etc.)

dirty_data_set = 'https://raw.githubusercontent.com/Benson90/602-Assignment/main/movies.csv'
df_dirty = pd.read_csv(dirty_data_set)

print(df_dirty['GENRE']) 
# found many new line in this column
#remove \n  

df_dirty['GENRE'] = df_dirty['GENRE'].str.replace("\n","").str.strip()     
print(df_dirty['GENRE']) 