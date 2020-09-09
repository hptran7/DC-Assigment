# Assignment 1 - Calculator - 

# In this assignment you are going to build a calculator. You are going to take three inputs from the user.  

# Input 1 - Represents the first number 

# Input 2 - Represents the operand (+, - , * , /) 

# Input 3 - Represents the second number 

# Based on the operand you are going to perform the math operation and print the result on the terminal. 

# - Make sure each math operation is a separate function. 

def add(num1, num2):
    return num1 +num2
def sub(num1,num2):
    return num1- num2
def mul(num1, num2):
    return num1 * num2
def div(num1, num2):
    return num1/num2
    
number1 = float(input("Please enter your first number: "))
number2 = float(input("Please enter your second number: "))
operand = input("Please enter you operand: ")
if operand == "+":
    print(add(number1,number2))
elif operand == "-":
    print(sub(number1,number2))
elif operand =="*":
    print(mul(number1,number2))
elif operand =="/":
    print(div(number1,number2))
