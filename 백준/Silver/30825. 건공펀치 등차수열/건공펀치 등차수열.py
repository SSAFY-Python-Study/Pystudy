N, K = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
for i in range(1, N):
    diff = arr[i] - arr[i - 1]
    if diff > K:
        arr[i - 1] += diff - K
        cnt += diff - K + ((diff - K) * (i - 1))
    else:
        arr[i] += K - diff
        cnt += K - diff
print(cnt)
