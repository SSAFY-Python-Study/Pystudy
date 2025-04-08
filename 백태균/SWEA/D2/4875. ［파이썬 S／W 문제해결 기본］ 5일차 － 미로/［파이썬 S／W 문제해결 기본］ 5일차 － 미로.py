# import sys
# sys.stdin = open('sample_input.txt', 'r')

def find_start():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                return i, j


def dfs(x, y):
    global found

    if arr[x][y] == 3:
        found = True
        return

    if found:
        return

    visited[x][y] = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and visited[nx][ny] == 0:
            dfs(nx, ny)

    return


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    x, y = find_start()
    visited = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    found = False
    dfs(x, y)

    if found:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')





