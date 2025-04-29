arr = list(map(int, input().split()))
check = [1, 1, 2, 2, 2, 8]
result = []

for i in range(len(arr)):
    result.append(check[i]-arr[i])

print(*result)
