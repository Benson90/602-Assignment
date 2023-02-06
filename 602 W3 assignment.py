#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 17:45:27 2023
602 week 3 assignment
@author: benson
"""
#Q1
print("Q1\n")
numbers = [1, 2, 3, 4, 5]
# It will return nothing, [1:-5] will be taking 2nd index from left and last 5 index. which logic error while the number list have only 5 index.
print(numbers[1:-5])

# To return entire list we can use below code
print(numbers[0:5])
print(numbers[0:])

#Q2
print("\nQ2\n")
# set variables
sales = []
total = 0

# Loop for sales number input and calculate the sum of sales
for i in range(1, 8):
    sales_amount = int(input("Enter day " +str(i)+" sales : $" ))
    total += sales_amount
    sales.append(sales_amount)

# Dispay sales list and total    
print("Sales in list", sales)
print("Sales in total", total)

#Q3
print("\nQ3\n")
places = ['Thailand', 'Japan', 'Mexico', 'Brazil', 'Taiwan']

print(places)

places.sort()

print(places)

places.sort(reverse=True)

print(places)

#Q4
print("\nQ4\n")
#import pandas
import pandas as pd

# pre-list
cn = ['602','607','608']
rn =  ['1111','1112','1113']
name = ['Brian','Shawn','Zeus']
time = ['Tuesday 13:10','Wednesday 15:10', 'Thursday 17:00']

# create dictionary
my_dict = {
    'Room Number':rn,
    'Instructors Name':name,
    'Meeting Time':time}

# Build a DataFrame 
program = pd.DataFrame(my_dict)

# Label index
program.index = cn

# Show all courses
print("Course list: ",cn)

# Input course number
course_name = input("Enter a course number: ")

# locate the course and display
print(program.loc[course_name])

#Q5
print("\nQ5\n")

# Dictionary of dictionaries
person = { 'Brian': { 'email':'Brian@gmail.com'},
           'Shawn': { 'email':'Shawn@hotmail.com'},
           'Zeus': { 'email':'Zeus@god.com'}}

print(person)
# Print out the email of Brian
print(person['Brian']['email'])

# Create sub-dictionary data
data = { 'email':'Daren@noreply.com' }

# Add data to person under key 'Daren'
person['Daren'] = data
print(person)
# Change person 'Daren' 's email
person['Daren']['email']='Daren@msn.com'
print(person)
# Remove person Shawn
del(person["Shawn"])

print(person)
