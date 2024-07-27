def checkTanSuat(lst, x):
    cnt = 0
    for i in lst:
        if i == x:
            cnt += 1
    return cnt
def checkSortList(lst):
    sorted_lst = sorted(lst)
    reversed_lst = sorted(lst, reverse=True)
    if lst == sorted_lst:
        return "Tăng"
    elif lst == reversed_lst:
        return "Giảm"
    else:
        return "NO"
    
if __name__ == '__main__':
    n = int(input("Nhập n: "))
    lst = []
    for i in range(n):
        val = int(input(f"Nhập phần tử thứ {i+1}: "))
        lst.append(val)
    print("Danh sách đã nhập:", lst)
    x = int(input("Nhập X: "))
    print(f"Tần suất xuất hiện của {x} trong danh sách là: {checkTanSuat(lst, x)}")
    #thay thế vị trí 2 đến 7
    lst[1:7]=[8, 5, 4, 0, 1, 3]
    print(f"New list :{lst}")
    print(f"min :{min(lst)}")
    print(f"max :{max(lst)}")
    Y=int(input("Nhap Y:"))
    lst.insert(0,Y)
    print(f"New list :{lst}")
    print(checkSortList(lst))
    new_lst = []
    for i in range(1, n + 1):
        new_lst.append(sum(lst[:i]))
    print("Newlist:", new_lst)

    new_lst2=[94, 39, 49, 6, -55, -37, 1, -23, -31, 1000]
    new_lst2=sorted(new_lst2)
    print(f"Tăng {new_lst2}")
    new_lst2=sorted(new_lst2,key=abs)
    print(f"Tăng theo abs:{new_lst2}")