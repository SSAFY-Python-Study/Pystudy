from collections import deque

M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
# print(arr)

q = deque()
# 이미 익은 토마토 찾기
for i in range(H):
    for j in range(N):
        for k in range(M):
            if arr[i][j][k] == 1:
                q.append([i, j, k])


# 토마토 익히기
def bfs():
    while q:
        i, j, k = q.popleft()
        for di, dj, dk in [[1, 0, 0], [0, 1, 0], [0, 0, 1], [-1, 0, 0], [0, -1, 0], [0, 0, -1]]:
            ni, nj, nk = i+di, j+dj, k+dk
            if 0<=ni<H and 0<=nj<N and 0<=nk<M and arr[ni][nj][nk] == 0:
                arr[ni][nj][nk] = arr[i][j][k] + 1
                q.append([ni, nj, nk])


bfs()

def counting_day():
    day_cnt = 0
    for a in range(H):
        for b in range(N):
            for c in range(M):
                if arr[a][b][c] == 0:
                    return -1

            else:
                day_cnt = max(day_cnt, max(arr[a][b]))
    return day_cnt -1

print(counting_day())
