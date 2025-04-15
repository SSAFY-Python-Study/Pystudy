N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 0
s = e = 0
for i in range(len(arr)):
    if e <= arr[i][0]:
        cnt += 1
        s, e = arr[i]
print(cnt)