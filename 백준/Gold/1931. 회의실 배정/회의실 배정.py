N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda k:(k[1], k[0]))
ans = 0
end = 0
for i in range(N):
    if end <= arr[i][0]:
        ans += 1
        end = arr[i][1]
print(ans)