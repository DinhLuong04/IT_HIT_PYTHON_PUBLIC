def tonguoc(n):
    sum = 0
    for i in range(1, n ):
        if n % i == 0:
            sum += i
    return sum

def check_amicable(n):
    cap_so = []
    for i in range(1, n + 1):
        j = tonguoc(i)
        if j > i and j <= n and tonguoc(j) == i:
            cap_so.append((i, j))
    return cap_so

n = int(input("Nhập n: "))
DS_cap = check_amicable(n)

print(f"Các cặp số Amicable từ 1 đến {n} là:")
for cap in DS_cap:
    print(f"{{{cap[0]},{cap[1]}}}")
