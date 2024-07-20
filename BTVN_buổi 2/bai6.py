def soHoanHao(n):
    sum=0
    for i in range (1,n):
        if(n%i==0):
            sum+=i
    if(sum==n):
        return True
  
  
n=int(input("Nhập n :"))
for i in range(1,n+1):
    if soHoanHao(i):
        print(i)