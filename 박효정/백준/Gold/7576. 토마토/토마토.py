from collections import deque

def bfs(arr):
    q = deque()
    visited = [[0]*M for _ in range(N)]

    # 시작점 찾기
    all_riped = True
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                visited[i][j] = 1
                q.append([i, j])
            elif arr[i][j] == 0:
                all_riped = False

    if all_riped: # 모든 토마토가 처음부터 익어있다면 (0이 하나도 없다면)
        return 0

    while q:
        i, j = q.popleft()

        for di, dj in [[-1,0], [0,1], [1,0], [0,-1]]:
            ni, nj = i + di, j + dj
            if 0<= ni <N and 0<= nj <M and visited[ni][nj] == 0 and arr[ni][nj] != -1:
                q.append([ni, nj])
                visited[ni][nj] = visited[i][j] + 1

    max_val = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                return -1
            if visited[i][j] > max_val:
                max_val = visited[i][j]

    return max_val - 1


M, N = map(int, input().split()) # 가로 M, 세로 N
tomato = [list(map(int, input().split())) for _ in range(N)]

# 처음부터 모든 토마토가 익어있다면 0
result = bfs(tomato)

# 토마토가 모두 익지 못하면 -1
print(result)