from collections import deque

def bfs(i, j):
    visited = [[0] * m for _ in range(n)]
    q = deque()
    q.append((i, j))
    cnt = 0
    visited[i][j] = 1

    while q:
        x, y = q.popleft()

        for dd in range(4):
            nx = x + dx[dd]
            ny = y + dy[dd]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0 and arr[nx][ny] == 'L':
                visited[nx][ny] = visited[x][y] + 1
                if visited[nx][ny] > cnt:
                    cnt = visited[nx][ny]

                q.append((nx, ny))

    return cnt - 1


n, m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
max_cnt = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            cnt = bfs(i, j)

            if cnt > max_cnt:
                max_cnt = cnt

print(max_cnt)