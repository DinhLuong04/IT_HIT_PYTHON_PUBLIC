k=int(input("Nhap K:"))
a=[]
for i in range(k):
        val = int(input(f"Nhập phần tử thứ {i+1}: "))
        a.append(val)
print("Danh sách đã nhập:", a)
n=int(input("Nhập n:"))
m=int(input("Nhập m:"))
if n * m != k:
        print("NO")
else:
        sublists = [a[i*m:(i+1)*m] for i in range(n)]
        print("Matrix {n} x {m}:")
        for sublist in sublists:
            print(sublist)