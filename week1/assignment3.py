# Take input from the user. If the input is divisible by 3 
# then print "Fizz", if the input it divisible by 5 then print "Buzz". 
# If the input is divisible by 3 and 5 then print "Fizz Buzz". 
num = float(input("Please enter your number: "))
while num%3 != 0 and num%5 != 0:
    num = float(input("Please enter a different number: "))
if num%3 == 0 and num%5 != 0:
    print("Fizz")
elif num%3 !=0 and num%5 ==0:
    print("Buzz")
elif num%3 ==0 and num%5 ==0:
    print("Fizz Buzz")
else:
    print("Your number is not correct") 