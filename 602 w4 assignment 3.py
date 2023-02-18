#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 11:18:56 2023
Assignment 3
@author: benson
"""

# Q1
def menu ():
    print("1. Breakfast")
    print("2. Lunch")
    print("3. Dinner")
    print("4. Exit")
    
done = False
while not done:
    menu()
    selected_menu = input()
    if selected_menu == "1":
        print("How about some bacon and eggs?")
    elif selected_menu == "2":
        print("How about wraps and sandwiches?")
    elif selected_menu == "3":
        print("How about steak?")
    elif selected_menu == "4":
        print("Thank you and Bye!")
        done = True
    else:
        print("Please select from the menu.")

#Q2
print("Enter work hours")
work_hours = float(input())
print("Enter rate of pay")
rate_per_hour = float(input())

if work_hours >= 20:
    gross_pay = 20 * rate_per_hour
    gross_pay = gross_pay + ((work_hours-20) * (rate_per_hour * 1.5))
else:
    gross_pay = work_hours * rate_per_hour
   
print("Your gross pay is $ " +str(gross_pay))


#Q3
def times_ten (x):
    print(x*10)
    
print("Input a number")
number = float(input())
times_ten(number)


#Q4
# debug: variable name change to lower case.
def main():
      calories1 = float(input( "How many calories are in the first food?"))
      calories2 = float(input( "How many calories are in the second food?"))
      showCalories(calories1, calories2)


# debug: input arguments, calculate and formatted float outside of print fucntion.
def showCalories(calories1,calories2):
    calories = calories1+calories2 
    formatted_calories= "{:.2f}".format(calories)
    print("The total calories you ate today " +str(formatted_calories))


main()

#Q5
def main():
    numerator = 1
    denominator = 30
    faction = 0
    while numerator <= 30:
        print (numerator, denominator)
        faction += (numerator / denominator)
        numerator += 1
        denominator -= 1

    print('Total:', faction)
main()


#Q6

def area_triangle (x,y):
    print("Area of triangle is: ", 0.5*x*y)


area_triangle(10,5)