from collections import deque

def bfs(arr):
    q = deque()
    visited = [[[0]*M for _ in range(N)] for _ in range(H)]

    # 시작점 찾기
    all_riped = True
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    visited[h][i][j] = 1
                    q.append([h, i, j])
                elif arr[h][i][j] == 0:
                    all_riped = False

    if all_riped: # 모든 토마토가 처음부터 익어있다면 (0이 하나도 없다면)
        return 0

    while q:
        h, i, j = q.popleft()

        for dh, di, dj in [[0,-1,0], [0,0,1], [0,1,0], [0,0,-1], [-1,0,0], [1,0,0]]:
            nh, ni, nj = h + dh,  i + di, j + dj
            if 0<= ni <N and 0<= nj <M and 0<= nh <H and visited[nh][ni][nj] == 0 and arr[nh][ni][nj] != -1:
                q.append([nh, ni, nj])
                visited[nh][ni][nj] = visited[h][i][j] + 1

    max_val = 0
    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 0 and visited[h][i][j] == 0:
                    return -1   # 토마토가 모두 익지 못하면 -1
                if visited[h][i][j] > max_val:
                    max_val = visited[h][i][j]

    return max_val - 1


M, N, H = map(int, input().split()) # 가로 M, 세로 N, 상자 수 H
tomatoes = []

for h in range(H):
    tomato = [list(map(int, input().split())) for _ in range(N)]
    tomatoes.append(tomato)

result = bfs(tomatoes)

print(result)