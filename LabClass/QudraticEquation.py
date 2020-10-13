#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 21:52:15 2020

@author: jumman
"""

def UserInput():
    while True:
        try:
            a = float(input("Enter your Value:" ))
            return a
            break
        except ValueError:
            print("Oops! that was not valid number. Try again...")

def GetDeta(a,b,c):
    delta = b**2 - (4*a*c)
    return delta

# def GetRoot(a,b,delta):
#     try:
#         root1 = (-b+(delta**0.5))/2*a
#         root2 = (-b-(delta**0.5))/2*a
#         return root1, root2
#     except:
#         print("Invalid data, divided by zero Error")

def main():
    variable_a = UserInput()
    variable_b = UserInput()
    variable_c = UserInput()
    try:
        variable_delta =GetDeta(variable_a, variable_b, variable_c)
        print("delta: ", variable_delta)
        if (variable_delta > 0):
            root_X1 = (-variable_b+(variable_delta**0.5))/(2*variable_a)
            root_X2 =(-variable_b-(variable_delta**0.5))/(2*variable_a)
            # it doesnot divide with 2a
            #problem was proper bracet 
            print("your two roots are:", root_X1, root_X2)
        elif (variable_delta == 0):
            root_X1 = -variable_b/(2*variable_a)
            print("There is only one root of this equation: ",root_X1 )
        else:
            print("There are no real root for this equation")
    except:
        print("invalid Calculation,try again...")

main()

# doesn't run at -5,10,16
#problem solved