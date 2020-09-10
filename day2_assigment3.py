def prime_check(num):
    n = 2
    prime = True
    while n < num:
        if num % n == 0:
            prime = False
            break
        n+= 1
    if prime == True and num>1:
        return "Your number is a Prime"
    else:
        return "Your number is not a prime number"
number=int(input("Please enter your number: "))
print(prime_check(number))