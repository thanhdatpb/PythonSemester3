# Cau 1

m = int(input("Nhập số phần tử của mảng: "))
a = []
for i in range(0, m):
    a.append(input('Nhập số thứ %d: ' % (i+1)))

print("Giá trị của mảng:")
for i in range(0, m):
    print(a[i], end="   ")
    

print("\n\n")
# Cau 2

n = -1
while (n <= 0):
    n = int(input("Nhập vào n>0: "))

# Chuyển từ thập phân sang nhị phân
x = n
kq = ""
while (n > 0):
    kq = str(n % 2)+kq
    n = n//2

print("Kết quả chuyển %d sang nhị phân : " % (x), kq)


print("\n\n")
# Cau 3

arrfib = []


def fib(a):
    first = 1
    second = 1
    if (a == 1 or a == 2):
        return 1
    for i in range(3, a+1):
        second = first + second
        first = second - first
    return second


a = -1
while (a <= 0):
    a = int(input("Nhập vào n > 0: "))

for i in range(1, a+1):
    arrfib.append(fib(i))

print(arrfib)
