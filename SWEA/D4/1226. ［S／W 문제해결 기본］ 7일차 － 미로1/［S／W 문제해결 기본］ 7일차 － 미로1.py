from collections import deque

# 미로를 탈출해 보자
def run_maze(i, j):
    v = [[0]*16 for _ in range(16)]
    q = deque([[i, j]])
    v[i][j] = 1
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
            ni, nj = ti+di, tj+dj
            if 0<=ni<16 and 0<=nj<16 and maze[ni][nj] != 1 and v[ni][nj] == 0:
                q.append([ni, nj])
                v[ni][nj] = v[ti][tj] + 1

    return 0


for _ in range(1, 11):
    t = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    ans = run_maze(1, 1)
    # 출력
    print(f"#{t} {ans}")