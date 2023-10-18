
def nhap_ma_tran_2_chieu(hang, cot):
    """
    ham nhap vao ma tran va tra ve list da chieu
    """
    ma_tran = []
    for i in range(hang):
a = []
        for j in range(cot):
            print("\tPhan tu thu [{0}][{1}] la:".format(i+1, j+1), end=" ") 
            a.append(int(input()))
        ma_tran.append(a)
    return ma_tran


hang = int(input("Nhap vao so hang: "))
cot = int(input("Nhap vao so cot: "))
print("Nhap vao ma tran A: ")
matrix_a = np.array(nhap_ma_tran_2_chieu(hang, cot))
print("Nhap vao ma tran B:")
matrix_b = np.array(nhap_ma_tran_2_chieu(hang, cot))

matrix_c = np.add(matrix_a, matrix_b)

print("Ma tran A vua nhap la:")
print(matrix_a)
print("Ma tran B vua nhap la:")
print(matrix_b)
print("Ma tran C la:")
print(matrix_c)