def d(n):
    str_n = str(n)
    num = n
    for i in range(len(str_n)):
        num += int(str_n[i])
    return num

arr = [0] * 11000
for i in range(1, 11001):
    arr[i-1] = d(i)

arr.sort()
check = [i for i in range(1, 10001)]

for i in range(10000):
    if check[i] not in arr:
        print(check[i])