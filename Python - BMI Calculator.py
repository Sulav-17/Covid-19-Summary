#!/usr/bin/env python
# coding: utf-8

name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI>0:
    if(BMI<18.5):
        print(name +", you are under weight.")
    elif(BMI<=24.9):
        print(name +", you are normal weight.")
    elif(BMI<=29.9):
        print(name + ", you are overweight.")
    elif(BMI<=34.9):
        print(name +", you are obese.")
    elif(BMI<=39.9):
        print(name +", you are Severely Obese.")
    else:
        print("you are Morbidly Obese.")
else: 
    print("Enter Valid Input")






Under 18.5	Underweight	Minimal
18.5 - 24.9	Normal Weight	Minimal
25 - 29.9	Overweight	Increased
30 - 34.9	Obese	High
35 - 39.9	Severely Obese	Very High
40 and over	Morbidly Obese	Extremely High






