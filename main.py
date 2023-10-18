import math


def SNT(a):
    if (a < 2):
        return False
    if (a == 2):
        return True
    for x in range(2, int(math.sqrt(a))+1):
        if (a % x == 0):
            return False
    return True


a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
for i in range(a, b+1):
    if (SNT(i)):
        print(i)