A=[]
n = int(input('Nhập vào số hàng của ma trận:'))
n = int(input('Nhập vào số cột của ma trận:'))
for i in range(0,n):
    l=[]
    for j in range(0,m):
    print('Nhập phần tử hàng ', i+1, "cột ", j+1)
    x=int(input())
    l=l+[x]
    l.append(l)

for i in range(0,n):
    for j in range(0,m):  
        print(A[i], [j], )

