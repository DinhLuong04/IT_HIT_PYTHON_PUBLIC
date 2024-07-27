def danxen(s1, s2):
    # Đan xen các ký tự của s1 và s2
    s4 = ''.join([s1[i] + s2[i] for i in range(min(len(s1), len(s2)))])
    return s4

def doicho(s1, s2):
    # Đổi chỗ 2 ký tự đầu tiên của 2 chuỗi
    if len(s1) < 2 or len(s2) < 2:
        print("Cả hai chuỗi phải có ít nhất 2 ký tự để thực hiện việc đổi chỗ.")
        return s1, s2
    
    s1_swapped = s2[:2] + s1[2:]
    s2_swapped = s1[:2] + s2[2:]
    
    return s1_swapped, s2_swapped


   
    
if __name__ == "__main__":
    s1=input("Nhập S1:")
    s2=input("Nhập S2:")
    s1_reversed = s1[::-1]
    print("s1 reversed:", s1_reversed)
    while True:
            a = int(input("Nhập  a : "))
            b = int(input("Nhập  b : "))
            if 1 <= a < b <= len(s2):
                break
            else:
                print("Nhập lại")
    truoc = s2[:a-1]
    daochuoi = s2[a-1:b]
    sau = s2[b:]
    reversed = daochuoi[::-1]
    result = truoc + daochuoi + sau
    print("Chuỗi s2 sau khi đảo ngược phần từ vị trí a đến b:", result)

    s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
    print('chuỗi s3 là chuỗi s1 sau khi xóa các kí tự vị trí chẵn:',
s3)
    s4 = danxen(s1, s2)
    print("Chuỗi s4 đan xen các ký tự của s1 và s2:", s4)

    
    s1_swapped, s2_swapped = doicho(s1, s2)
    print("Chuỗi s1 sau khi đổi chỗ 2 ký tự đầu tiên:", s1_swapped)
    print("Chuỗi s2 sau khi đổi chỗ 2 ký tự đầu tiên:", s2_swapped)