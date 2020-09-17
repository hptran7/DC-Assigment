def max_number(number):
    num = number[0]
    for n in number:
        if n<num:
            num = n
    return num
print(max_number([10,3,48,5,6,7]))