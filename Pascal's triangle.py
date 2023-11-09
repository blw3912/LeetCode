rowIndex=16

row0 = [1]
row1 = [1, 1]
if rowIndex == 0:
    print(row0)
if rowIndex == 1:
    print(row1)

lastRow = row1
for rows in range(2, rowIndex+1):  # start by constructing row 2
    sumRow = []

    for i in range(len(lastRow) - 1):
        sumRow.append(lastRow[i] + lastRow[i + 1])
    #print sumRow
    lastRow = [1] + sumRow + [1]
    print(lastRow)