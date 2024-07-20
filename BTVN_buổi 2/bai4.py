def fibo(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n - 1) + fibo(n - 2)


n = int(input("Nhập n: "))
dem=1
while (dem<=n):
    print(f"số fibonaci thứ {dem} : {fibo(dem)}")
    dem+=1