N = int(input())

arr = dict()

for i in range(N):
    title = input()
    if title in arr:
        arr[title] += 1
    else:
        arr[title] = 1
ans = sorted(arr.items(), key=lambda x:(-x[1], x[0]))

print(ans[0][0])