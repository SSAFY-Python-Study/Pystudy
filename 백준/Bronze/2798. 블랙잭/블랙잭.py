N, M = map(int, input().split())    # N 카드의 수, M 합의 상한
arr = list(map(int, input().split()))   # 카드 숫자들
ans = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            if arr[i]+arr[j]+arr[k] > M:
                continue
            else:
                ans = max(ans, arr[i]+arr[j]+arr[k])

print(ans)