#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 14:47:48 2023
https://data.cityofnewyork.us/City-Government/NYC-Jobs/kpav-sd4t
@author: benson
"""

import pandas as pd
import matplotlib.pyplot as plt


# read the csv file into a pandas dataframe
df = pd.read_csv('NYC_Jobs.csv')

# display the first few rows of the dataframe
print(df.head())



# Data Wrangling 
# display the data type
print(df.dtypes)

# 1) Modify multiple column names.
rename_dict = {'# Of Positions': 'Number of Position', 'Full-Time/Part-Time indicator': 'Job Type'}
df = df.rename(columns=rename_dict)

# 2) Look at the structure of your data – are any variables improperly coded? Such as strings or characters? Convert to correct structure if needed.
# Convert the string to date data type
df['Posting Date'] = pd.to_datetime(df['Posting Date'])
df['Posting Updated'] = pd.to_datetime(df['Posting Updated'])
df['Process Date'] = pd.to_datetime(df['Process Date'])

# 3) Fix missing and invalid values in data.
# Check any Null Value and drop it in #6
print(df.isna().any(axis=0))

# Check number of records
num_rows = len(df)

# 4) Create new columns based on existing columns or calculations.
df['Average Salary'] = (df['Salary Range From'] + df['Salary Range To'] )/2
df['Job Category Type'] = df['Job Category'].str.extract('(\w+)')

# 5) Drop column(s) from your dataset.
# Drop Unused Column
df = df.drop('Post Until', axis=1)
df = df.drop('Recruitment Contact', axis=1)
df = df.drop('Work Location 1', axis=1)
df = df.drop('Additional Information', axis=1)
df = df.drop('Hours/Shift', axis=1)

# 6) Drop a row(s) from your dataset.
# Drop Nan Records
df = df.dropna()

# 6303 - 5164 = 1139 row removed for incomplete records 
num_rows_updated = len(df)

# 7) Sort your data based on multiple variables.
# 8) Filter your data based on some condition.
# create new dataframe for some specific analysis (filtering and sorting)
job_ft_salary_df = df[(df["Job Type"]=='F') & (df["Salary Frequency"] == "Annual")] 

job_ft_salary_df = job_ft_salary_df.loc[:, ['Job Category Type', 'Average Salary', 'Career Level']]
job_ft_salary_df = job_ft_salary_df.sort_values(["Job Category Type", "Average Salary"],ascending =[True,True])


# 9) Convert all the string values to upper or lower cases in one column.
job_ft_salary_df['Job Category Type'] = df['Job Category Type'].str.upper()


# 10) Check whether numeric values are present in a given column of your dataframe.
is_numeric = pd.to_numeric(job_ft_salary_df['Average Salary'], errors='coerce').notnull().all()


# 11) Group your dataset by one column, and get the mean, min, and max values by group.
#       Groupby()
#       agg() or .apply()
result = job_ft_salary_df.groupby('Job Category Type').agg({'Average Salary': ['mean', 'min', 'max']})

print(result)

# 12) Group your dataset by two columns and then sort the aggregated results within the groups.
result2 = job_ft_salary_df.groupby(['Job Category Type','Career Level']).agg({'Average Salary': ['mean', 'min', 'max']})

result2.plot(kind='bar', figsize=(10, 6))
plt.title('Aggregated Data by Two Columns')
plt.xlabel('Job Category Type')
plt.ylabel('Mean Value')
plt.show()