s = 'aab'
lists=[]
for x in s:
    lists.append(x)
print(lists)

subst = []

for x in range(len(lists)-1): #x = 0,1,2
    current = []
    n=x # n= 0,1,2
    while n<len(lists): # n < 2 !!
        if lists[n] not in current:
            current.append(lists[n])
        else:
            break
        n+=1
    subst.append(current)
print(subst)

answer = subst[0]
for _ in range(len(subst)):
    if len(subst[_]) > len(answer):
        answer = subst[_]
print(answer)
print(len(answer))

