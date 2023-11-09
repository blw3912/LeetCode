nums = [2,3,1,1,4]
print(nums)

final = len(nums) - 1

paths = [] #put possible paths in here as lists

pos = 0

for n in range(1, nums[pos] + 1):  # Ex/ for '2': add 1 or 2
    path = [pos]
    path.append(pos + n)
    paths.append(path)

#print(paths)

AllCopies = [] #store split-off copies here for each path that needs to branch
for path in paths:
    lastpos = path[-1]

    if nums[lastpos]>1: #replicate paths if entry > 1
        numCopies = nums[lastpos]-1
        #print(numCopies)
        Copies = (numCopies-1)*[path]
        print("Copies",Copies)
    AllCopies+=(Copies) # DONT WANT LIST WITHIN LIST HERE !!
print(AllCopies)

paths.append(AllCopies)
print(paths)

currentStop = [path[-1] for path in paths]
#print(currentStop)
