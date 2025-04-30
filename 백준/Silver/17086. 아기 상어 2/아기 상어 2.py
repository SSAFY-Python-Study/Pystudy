from sys import stdin as s

input = s.readline
delta = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

def BFS(si, sj):
    visited = [[0] * M for _ in range(N)]
    queue = [[si, sj]]
    visited[si][sj] = 1
    while queue:
        ti, tj = queue.pop(0)

        for di, dj in delta:
            ni, nj = ti + di, tj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                if ocean[ni][nj] == 1:
                    return visited[ti][tj]
                visited[ni][nj] = visited[ti][tj] + 1
                # ti, tj = ni, nj
                queue.append([ni, nj])
    return 0

N, M = map(int, input().split())
ocean = [list(map(int, input().split())) for _ in range(N)]
max_length = 0
for i in range(N):
    for j in range(M):
        if ocean[i][j] == 1:
            continue
        length = BFS(i, j)
        if max_length < length:
            max_length = length

print(max_length)