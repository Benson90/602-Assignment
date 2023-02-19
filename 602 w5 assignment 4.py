#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 18 17:19:41 2023
Assignment 4 week 5
@author: benson
"""
import math

#Q1

class BankAccount:  
#__init__attribute      
    def __init__(self, bankname, firstname, lastname, balance):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance
#Custom __str__        
    def __str__ (self):
        return 'Bank name : ' + str(self.bankname) + '\nName : ' + str(self.firstname) + ' ' + str(self.lastname) + '\nBalance : ' + str(self.balance)
#deposit function and deposit amount error check       
    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            return True
        return False
#withdrawal function and balance error check 
    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False        
#record        
alex_account = BankAccount("Chase", "Alex", "Lee", 0)
print("Q1\n")
print(alex_account.__str__())

#run method
if alex_account.deposit(1000):
    print("The deposit was successful, the balance is now", alex_account.balance)
else:
    print("The deposit was unsuccessful, the amount is less than 0")
    
    
if alex_account.withdrawal(500):
        print("The withdrawal was successful, the balance is now", alex_account.balance)
else:
        print("The withdrawal was unsuccessful, the balance is insufficient")
        
print(alex_account.__str__())
        
        
#Q2


class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width
            
    def __str__ (self):
        return 'Length : ' + str(self.length) + '\nWidth : ' + str(self.width) 

        
    def render(self):
        for x in range(self.length):
            for y in range(self.width):
                print('*',end='')
            print()
            
    def invert(self):
        temp = self.length
        self. length = self.width
        self.width = temp
        
    def get_area(self):
        return self.length*self.width
            
    def get_perimeter(self):
        return self.length*2 + self.width*2     
    
    def double(self):
        self.length = self.length*2
        self.width = self.width*2    
               
    def __eq__(self, other):
        return self.length == other.length and self.width == other.width
    
    def print_dim(self):
        print(self.__str__())  
    
    def get_dim(self):
        return self.length, self.width
    
    def combine(self, other):
        self.length = self.length + other.length 
        self.width = self.width + other.width
    
    def get_hypot(self):
        return math.sqrt(pow(self.length,2)+pow(self.width,2))    

box1 = Box(5,10)
box2 = Box(3,4)
box3 = Box(5,10)

print("\nQ2")

box1.print_dim()
box2.print_dim()
box3.print_dim()

print(box1 == box2)
print(box1 == box3)


box1.combine(box3)
box1.render()

box2.double()
print(box2.get_dim())

box1.combine(box2)
box1.render()
"""

testing... 

print(box1.__str__())

box1.render()

box1.invert()
print(box1.__str__())

print(box1.get_area())
print(box1.get_perimeter())

box1.double()
print(box1.__str__())




print(box1 == box2)

box1.print_dim()

print(box1.get_dim())

box1.combine(box2)
box1.print_dim()

print(box1.get_hypot())


"""












