import heapq

N = int(input())
ans = []

for i in range(N):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        if len(ans) == 0:
            print(-1)
        else:
            tmp = -heapq.heappop(ans)
            print(tmp)
    else:
        for j in range(arr[0]):
            heapq.heappush(ans, -arr[j+1])