nums = [2,1,1,2,3,3,4,2,5,5,6,7,8]

mine = []
for entry in nums:
    if entry not in mine:
        mine.append(entry)

print(mine)