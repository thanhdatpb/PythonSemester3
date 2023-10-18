def find_max(a, b, c):
    max = a
    if max < b: max = b
    if max < c: max = c
    return max
 
 
print("Nhập vào số thứ nhất: ")
a = float(input())

print("Nhập vào số thứ hai: ")
b = float(input())
 
print("Nhập vào số thứ ba: ")
c = float(input())
 
 
print("Số lớn nhất trong ba số "," là ", find_max(a, b, c))
