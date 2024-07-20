import sys
#(a)
def bits(a):
    return a.bit_length()

a = int(input("Nhập số a: "))
print(f"Số lượng các bits  là: {bits(a)}")
#(b)
x = "awesome"

# (f-string)
print(f"Python is {x}")

# format()
print("Python is {}".format(x))

#  nối chuỗi
print("Python is " + x)


#(c)
print(f"Phiên bản Python hiện tại là: {sys.version}")
