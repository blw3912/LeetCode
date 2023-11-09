# Given two binary strings a and b, return their sum as a binary string.

a = '11'
b = '1'

# convert to base 10
astr = str(a)
bstr = str(b)

tota = 0
for i in range(len(str(a))):
    tota += int(a[i])*2**(len(str(a))-(i+1))
print('tota:',tota)

totb = 0
for i in range(len(str(b))):
    totb += int(b[i])*2**(len(str(b))-(i+1))
print('totb:',totb)

total = tota + totb
print('total:',total)

#convert the total back, first find how many digits are needed using log
import math
if math.log(total,2) %1 ==0:
    digits = int(math.log(total,2)+1)
else:
    digits = int(math.ceil(math.log(total,2)))
print('digits:',digits)

bindigs = []
for i in range(digits):
    basepower = 2**(digits-(i+1))
    print(basepower)

    if basepower <= total:
        next = '1'
        total -= basepower
    else:
        next = '0'
    bindigs.append(next)

final = ''.join(bindigs)
print(final)
