def max_number(number):
    num = 0
    for n in number:
        if n>num:
            num = n
    return num
print(max_number([2,3,48,5,6,7]))