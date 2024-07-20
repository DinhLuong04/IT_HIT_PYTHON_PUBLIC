
a = int(input("Nhập  a: "))
b = int(input("Nhập  b: "))

#(a)
print("a + b =", a + b)

#(b)
print("a - b =", a - b)

#(c)
print("a * b =", a * b)

#(d)
if b != 0:
    print("a // b =", a // b)
else:
    print("Không thể chia cho 0")

#(e)
print("a ** b =", a ** b)

#(f)
if b != 0:
    print("a % b =", a % b)
else:
    print("Không thể chia cho 0")

#(g)
if a > b:
    print("a lớn hơn b")
elif a < b:
    print("a nhỏ hơn b")
else:
    print("a bằng b")

#(h)
print("a AND b =", a & b)

#(i)
print("a OR b =", a | b)

#(j)
print("a XOR b =", a ^ b)

#(k)
print("NOT a == b:", not a == b)

#(l)
print("a dịch phải 1 đơn vị:", a >> 1)

#(m)
print("a dịch trái 1 đơn vị:", a << 1)
