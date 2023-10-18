#Viết chương trình nhập vào một số nguyên n, in ra màn hình tổng các ước số của n
#(không kể n).
# Input: n=10
# Output: S=1+2+5=8
n = int(input())

sum = 0
print("Nhap so nguyen n: ")
for i in range(1, n+1):
  if (n % i == 0):
    sum += i
print("Tong cac uoc so cua", n, " la: ", sum)

# Viết hàm trả về khoảng cách giữa 2 điểm A(x A ,y A ) và B(x B , y B ) trong mặt phẳng cho
# trước theo công thức kc(A,B)=.
# Áp dụng hàm trên, viết chương trình nhập vào tọa độ 2 điểm, in ra màn hình khoảng
# cách của 2 điểm đã cho.
def kc(a1, b1, a2, b2):
    return math.sqrt((pow(a1-a2, 2) + pow(b1-b2, 2)))


print("\n\tCâu 2:")
print("Nhập tọa độ điểm A:")
a1 = int(input("a1 = "))
a2 = int(input("a2 = "))
print("Nhập tọa độ điểm B:")
b1 = int(input("b1 = "))
b2 = int(input("b2 = "))
print("Khoảng cách giữa 2 điểm A và B là: %0.2f" % kc(a1, a2, b1, b2))

#Viết chương trình nhập vào một danh sách A có n phần tử số nguyên, sau đó:
# a. Nhập vào một số nguyên x, in ra màn hình số lượng các phần tử có giá trị
# bằng x.
# b. In ra màn hình phần tử đầu tiên có giá trị lớn nhất và vị trí của nó.
# c. In ra màn hình danh sách sau khi đã sắp xếp các giá trị trong danh sách A theo
# thứ tự tăng dần.
n = int(input("\n\tCâu 3: Nhập số phần tử của mảng: "))
a = []
for i in range(0, n):
    a.append(input('Nhập số thứ %d: ' % (i+1)))

print("\tMảng vừa nhập :")
for i in range(0, n):
    print(a[i], end="   ")

x = int(input("\n\tCâu 3a: Nhập giá trị x: "))
dem = 0
for i in range(0, n):
    if (int(a[i]) == x):
        dem += 1
print("\tMảng có %d phần tử = %d" % (dem, x))

print("\tCâu 3b: Phần tử lớn nhất trong mảng là %d" % int(max(a)))
print("\tCâu 3c: Giá trị của mảng sau khi sắp xếp tăng dần :")
a.sort()
for i in range(0, n):
    print(a[i], end="   ")


# Viết chương trình tính tổng các ký tự có trong một chuỗi cho trước
# Input: “CNTT_K45A” 
# Ouput: 9
chars = "CNTT_K45A"
 
for char in chars:
  len = check_string.len(char)
  if len > 1:
    print(char, len)


# Viết chương nhập vào một chuỗi, in ra màn hình từ có chiều dài lớn nhất số từ của
# chuỗi đã cho.
# Input: “Programming Java in oj”
# Output: Programming
def chuoi(s):
    s1=s.split()
    lst=''
    for i in s1:
        if len(i)>len(lst):
            lst=i
    return lst
while True:
    s=input('Nhập chuỗi s: ',)
    print(chuoi(s))