def ChuanHoaTen(name):
    Ten = ' '.join(name.split())
    ChuanHoa = Ten.title()
    return ChuanHoa

if __name__ == "__main__":
    name = input("Nhập họ và tên: ")
    NewName = ChuanHoaTen(name)
    print("Tên đã chuẩn hóa:",NewName)
