class hoadon:
    def __init__(self, makh = None, hoten = None, diachi = None, chisocu = None, chisomoi = None):
        self.makh = makh
        self.hoten = hoten
        self.diachi = diachi
        self.chisocu = chisocu
        self.chisomoi = chisomoi

    def nhap(self):
        self.makh = input("Mã khách hàng: ")
        self.hoten = input("Họ tên: ")
        self.diachi = input("Địa chỉ: ")
        self.chisocu = int(input("Chỉ số cũ:"))
        self.chisomoi = int(input("Chỉ số mới:"))
    def xuat(self):
        print("Mã khách hàng:", self.makh)
        print("Họ tên:", self.hoten)
        print("Địa chỉ: ", self.diachi)
        print("Chỉ số cũ: ", self.chisocu)
        print("Chỉ số mới: ", self.chisomoi)
        print("Số lượng điện tiêu thụ: ", self.sldtieuthu())
    def get_makh(self):
        return self.makh
    def get_hoten(self):
        return self.hoten
    def get_chisocu(self):
        return self.chisocu
    def get_chisomoi(self):
        return self.chisomoi
    def sldtieuthu(self):
        ldtthu = self.chisomoi - self.chisocu
        return ldtthu
    def __gt__(self, orther):
        if(self.sldtieuthu() > orther.sldtieuthu()):
            return True
        else:
            return False*2

    def Check(DS, ma, k):
        for i in range(k):
            if DS[i].makh == ma:
                return False
        return True
DS = []
x = 0
while(x == 0):
    n = int(input("Nhập vào số lượng n: "))
    if (n > 0 and n <= 50):
     x = 1
    else:
        print("Số lượng học phần phải lớn hơn 0 và nhỏ hơn 50!")
        x = 0
for i in range(0,n):
    hd = hoadon()
    hd.nhap()
    DS.append(hd)