list1 = [1,2,3]
list2 = [2,3,4]

merged = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] < list2[j]:
            merged.append(list1[i])
        else:
            merged.append(list2[j])
print(merged)