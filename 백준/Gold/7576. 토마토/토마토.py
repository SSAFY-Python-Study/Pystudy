from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

# 익은 토마토 좌표 인큐
q = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            q.append([i, j])
# print(q)


# BFS
def bfs():
    while q:
        i, j = q.popleft()
        for di, dj in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                # 1씩 더해주면 몇 번째 날 토마토가 익었는지 알 수 있다!
                arr[ni][nj] = arr[i][j] + 1
                # 익은 토마토를 인큐하고 그 위치에서 bfs가 이어지게 하기
                q.append([ni, nj])

bfs()

cnt = 0
for k in arr:
    # bfs로 토마토 익히는 과정 끝냈는데도 안 익음 -> 안되는 것임(-1)
    if 0 in k:
        print(-1)
        exit(0)
    # arr에서 마지막으로 토마토가 익은 날짜 = 한 행에서 최댓값을 찾아 갱신하다보면 나옴
    else:
        cnt = max(cnt, max(k))

# arr[i][j]가 1일 때부터 시작했으므로, -1해야 원하는 값이 나옴
print(cnt-1)