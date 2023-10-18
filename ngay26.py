# Viết chương trình nhập vào một danh sách A có n phần tử số nguyên, sau đó tạo ra một danh sách B chứa các số nguyên ngược lại với A(lưu ý mảng A không thay đổi giá trị)

m = int(input("Nhập số phần tử của mảng: "))
a = []
for i in range(0, m):
    a.append(input('Nhập số thứ %d: ' % (i+1)))

print("Giá trị của mảng:")
for i in range(0, m):
    print(a[i], end="   ")



print("\n\n")

# Viết hàm chuyển đổi một nguyên dương ở hệ thập phân sang nhị phân. Áp dụng hàm trên, viết chương trình nhập vào một số nguyên n ( n< 0) ở hệ thập phân ,
# in ra màn hình kết quả sau khi chuyển đổi sang hệ nhị phân.


n = -1
while (n<=0):
    n = int(input("Nhập vào n>0: "))

# Chuyển từ thập phân sang nhị phân
x = n
ketQua = ""
while(n>0):
    ketQua = str(n%2)+ketQua
    print("n%2 = ", n%2)
    n = n//2
    print("n = ", n)

print("Kết quả: ", ketQua)
#  Viết hàm trả về số Fibonaci thứ n (n>0)  ( với n là số nguyên dương cho trước)

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
