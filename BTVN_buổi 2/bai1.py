# a
n=int(input("Nhap n :"))
tmp=n
tong=0
while (tmp!=0):
    tong+=tmp%10
    tmp=tmp//10
print("Tong cac chu so :",tong)

# b
tongUoc=0
for i in range(1,n+1):
    if(n%i==0):
        tongUoc+=i
print("Tong uoc :",tongUoc)

# c
a=int(input("Nhap a : "))
b=int(input("Nhap b : "))
c=int(input("Nhap c : "))

if(a+b>c and a+c> b and b+c>a):
        print("Hinh tam giac")
        if(a==b and b==c):
            print("Tam giac deu")
        elif(a==b or a==c or b==c):
             print("tam giac can")
        elif(a**a==b**b+c**c or b*b==a*a+c*c or c*c ==a*a+b*b):
             print(" tam giac vuong")
        elif(a**a>b**b+c**c or b*b>a*a+c*c or c*c >a*a+b*b):
            print("tam giac tu")
        else:
             print("tam giac nhon")
else:
     print("khong phai tam giac")
    