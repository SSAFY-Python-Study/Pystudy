from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dq = deque()
max_v = 0

# 시작점 큐에 담기
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            # 인큐
            dq.append((i, j))

# BFS
while dq:
    # 디큐
    i, j = dq.popleft()
    # 상하좌우 델타 함수 적용
    for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ni, nj = i + di, j + dj
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == 0:
            # 인큐
            dq.append((ni, nj))
            arr[ni][nj] = arr[i][j] + 1
            max_v = arr[ni][nj] - 1

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print(-1)
            break
    else:
        continue
    break
else:
    print(max_v)
