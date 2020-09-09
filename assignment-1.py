def add(num1, num2):
    return num1 +num2
def sub(num1,num2):
    return num1- num2
def mul(num1, num2):         
    return num1 * num2
def div(num1, num2):
    return num1/num2
def math(num1,num2,fn):
    return fn(num1,num2)
number1 = float(input("Please enter your first number: "))
number2 = float(input("Please enter your second number: "))
operand = input("Please enter you operand: ")
operand_dict = {
     "+": add,
     "-":sub,
     "*": mul,
     "/": div
 }

fun = operand_dict[operand]
print(math(number1,number2,fun))
