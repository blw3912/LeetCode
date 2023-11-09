x = 121

from math import floor

def myfunc(x):
    mine = str(x)
    lst=[i for i in mine]

    for _ in range(int(floor(len(mine)/2))):
        if mine[_] != mine[-(_+1)]:
            return False
    return True

print(myfunc(123521))

