from collections import deque

def bfs():
    # 초기 값 설정
    dq = deque()
    max_day = 0
    # 시작점 설정
    is_completed = True
    for k in range(H):
        for i in range(N):
            for j in range(M):
                if arr[i + k*N][j] == 1:
                    # 인큐
                    dq.append((i, j, k))
                if arr[i + k*N][j] == 0:
                    is_completed = False
    # 안 익은 토마토가 없으면 0 반환
    if is_completed:
        return 0
    while dq:
        # 디큐
        i, j, k = dq.popleft()
        # 상하좌우앞뒤 순서로 델타 함수 적용
        for di, dj, dk in [(-1, 0, 0), (1, 0, 0),
                           (0, -1, 0), (0, 1, 0),
                           (0, 0, -1), (0, 0, 1)]:
            ni, nj, nk = i + di, j + dj, k + dk
            # 인덱스를 벗어나지 않았을 때
            if 0 <= ni < N and 0 <= nj < M and 0 <= nk < H:
                idx = ni + nk*N
                # 방문하지 않았을 때
                if arr[idx][nj] == 0:
                    # 인큐
                    dq.append((ni, nj, nk))
                    arr[idx][nj] = arr[i + k*N][j] + 1
                    max_day = arr[idx][nj]
    # 안 익은 토마토가 있는지 확인
    for k in range(H):
        for i in range(N):
            for j in range(M):
                # 안 익은 토마토가 있으면 -1 반환
                if arr[i + k*N][j] == 0:
                    return -1
    return max_day - 1

M, N, H = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N * H)]
result = bfs()
print(result)