from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(start_x, start_y):
    global result
    q = deque()
    q.append((start_x, start_y))
    visited[start_x][start_y] = 1

    while q:
        x, y = q.popleft()

        if arr[x][y] == 3:
            result = True
            return

        for di in range(4):
            nx = x + dx[di]
            ny = y + dy[di]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if visited[nx][ny] == 0 and arr[nx][ny] != 1:
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return


for tc in range(1, 11):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    result = False

    bfs(1, 1)

    if result:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')