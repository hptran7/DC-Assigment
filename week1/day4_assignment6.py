def drawing(symbol,size):
    count =1
    space =1
    count2 = 1
    space2 = int(size)/2
    while count < int(size):
        print(" "*(18-space) + symbol *count)
        count +=2
        space +=1
    while count2 <int(size):
        print(" "*int(space2) + symbol*(18-count2))
        count2 +=2
        space2 +=1
drawing("*",18)