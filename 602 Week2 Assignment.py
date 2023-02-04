#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  4 16:15:35 2023

@author: benson
"""

#Q1 Fix all the syntax and logical errors in the given source code 
#add comments to explain your reasoning

# This program gets three test scores and displays their average.  It congratulates the user if the 
# average is a high score. The high score variable holds the value that is considered a high score.

# Set to lower case variable 
high_score = 95
 
# Get the test scores.
test1 = input('Enter the score for test 1: ')
test2 = input('Enter the score for test 2: ')
# Missing test3 variable and input
test3 = input('Enter the score for test 3: ')
# Calculate the average test score.
# Change the variable type to perform calculation
# Calculation logic error. (Math order of operations: PEMDAS) add all test scores then divide to find the average.
average = (float(test1) + float(test2) + float(test3)) / 3
# Print the average.
# round up the float number to make it look clean
print('The average score is', round(average,2))
# If the average is a high score,
# congratulate the user.
if average >= high_score:
    print('Congratulations!')  
else:
    print('That is a great average!')

#Q2
#The area of a rectangle is the rectangle’s length times its width. Write a program that asks for the length and width of two rectangles and prints to the user the area of both rectangles. 

# Get the length and width
length = input('Enter the rectangle\'s length: ')
width = input('Enter the rectangle\'s width: ')

# Calculate the area
area = (float(length) * float(width))

# Print the area
print('The area of a rectangle is', round(area,2))


#Q3 
#Ask a user to enter their first name and their age and assign it to the variables name and age. 
#The variable name should be a string and the variable age should be an int.  

first_name = input('Enter your first name: ')
age = input('Enter your age: ')

# Change variable type to Int
age = int(age)

#Using the variables name and age, print a message to the user stating something along the lines of:
# "Happy birthday, name!  You are age years old today!"

# Print variable first name and change variable age to string for print. 
print("Happy birthday, " +first_name+ "!  You are "+str(age)+" years old today!")