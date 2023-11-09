digits = [1,2,3,4]

mystr = ''
for i in digits:
    mystr += str(i)
print(mystr)
number = int(mystr)
newnum = number+1
numstr = str(newnum)

final = [int(i) for i in numstr]
print(final)


# '1234'