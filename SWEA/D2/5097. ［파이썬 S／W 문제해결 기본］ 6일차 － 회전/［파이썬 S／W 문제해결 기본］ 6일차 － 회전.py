from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque(arr)

    for i in range(M):
        q.append(q.popleft())

    print(f'#{tc} {q[0]}')