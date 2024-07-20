import math

# Tính tổng S(n) = 1 - 2 + 3 - 4 + 5 + .... + (2*n + 1)
def tong1(n):
    sum1 = 0
    for k in range(n + 1):
        sum1 += (-1)**k * (k + 1)
    return sum1

# Tính tổng S(n) = 1 + 1/2 + 1/3 + .... + 1/n
def tong2(n):
    sum2 = 0.0
    for k in range(1, n + 1):
        sum2 += 1 / k
    return sum2

# Biện luận nghiệm của phương trình bậc hai ax^2 + bx + c = 0
def PTBacHai(a, b, c):
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    elif delta == 0:
        x = -b / (2*a)
        return f"Phương trình có nghiệm kép: x = {x}"
    else:
        return "Phương trình vô nghiệm "

# Nhập giá trị cho n và hệ số a, b, c
n = int(input("Nhập giá trị n: "))
a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))

# Tính tổng và biện luận nghiệm
S1= tong1(n)
S2 = tong2(n)
phuongTrinhBacHai = PTBacHai(a, b, c)

# In kết quả
print(f"Tổng 1 là: {S1}")
print(f"Tổng 2 là: {S2}")
print(f"PT Bậc 2 là :{phuongTrinhBacHai}")
