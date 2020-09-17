names = ["Alex","John","Mary","Steve","John", "Steve"]
name_check=[]
for n in names:
    if not n in name_check:
        name_check.append(n)
names= name_check
print(names)