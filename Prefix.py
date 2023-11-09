# if first index matches for every string, append str with that letter
# check if strs[0][0] = strs[1][0] = ... = strs[w][0] -> str+strs[0][0]
# check if strs[0][1] = strs[1][1] = ... = strs[w][1] -> str+strs[0][1]
# ....
# check if strs[0][l] = strs[1][l] = ... = strs[w][l] -> str+strs[0][l]

strs = ['Theballs','Thebrapy','Thebsaurus','Thebrmopolis']

minlength = min([len(strs[i]) for i in range(len(strs))])

l=0

while l in range(minlength):
    match = True
    for w in range(len(strs)):
        if strs[0][l] != strs[w][l]:
            match = False
    if match:
        l+=1
    else:
        break

print(strs[0][:l])

