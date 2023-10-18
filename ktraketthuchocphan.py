#cau 1
def check(a):
	b=a.split()
	return b[-1]
a=[]
while True:
	n=str(input("nhap ten sinh vien: "))
	if(n==""):
		break
	a.append(n)
for i in a:
	if check(i)=="Anh":
		print(i)  

l=[]
n=int(input("nhap n: "))
for i in range(0,n):
	a=str(input("nhap ma hoc phan: "))
	b=str(input("nhap ten hoc phan: "))
	c=int(input("so tin chi: "))
	d={
		'mahp':a,
		'tenhp':b,
		'sotc':c
	}
	l.append(d)
for i in l:
	a=i['mahp']
	if a[0:3]=="TIN":
		print("mahp: ",i['mahp'])
		print("tenhp: ",i['tenhp'])
		print("sotc: ",i['mahp'])
		print("------------------")
st=str(input("nhap chuoi: "))
size=len(st)
for i in l:
	a=i['tenhp']
	if(a[0:size]==st):
		print(i['tenhp'])


