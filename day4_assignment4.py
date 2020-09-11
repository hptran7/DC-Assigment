def dup(*number):
    check_list=[]
    original = [0,1,2,3,4,5,6,7,8,9]
    number = list(number)
    for n in original:
        if not n in number: 
            check_list.append(n)
    return check_list

print(dup(1,2,3,4,5,5))