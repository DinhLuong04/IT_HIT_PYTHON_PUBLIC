n=int(input('Nhap:'))
list=[]
listRes=[]
for i in range(0,n):
    i=int(input(f'Nhập số thứ {i+1}:'))
    list.append(i)

for i in range(len(list)):
    if list.count(list[i])%5==0 and (list[i])%10 !=0:
        listRes.append(list[i])
setRs=set(listRes)
Tp=tuple(setRs)
print(Tp)


