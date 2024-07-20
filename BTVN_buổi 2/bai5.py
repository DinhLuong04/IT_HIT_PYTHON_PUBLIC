def checkArmstrong(n):
    tmp=n
    sum=0
    
    while(tmp!=0):
        r=tmp%10
        sum+=(r*r*r)
        tmp//=10
    if(n==sum):
        return True
    else:
        return False

n=int(input("Nhập n :"))
for i in range(1,n+1):
    if checkArmstrong(i):
        print(i)
    



