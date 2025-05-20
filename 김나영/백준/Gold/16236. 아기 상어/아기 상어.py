import sys

input = sys.stdin.readline

def bfs(si, sj):
    visited = [[0] * N for _ in range(N)]
    queue = [[si, sj]]
    available = []
    shark = 2
    second = 0
    ate = 0
    flag = True

    while flag:
        flag = False
        if available:
            min_i, min_j = available[0][0], available[0][1]
            min_distance = visited[min_i][min_j]
            for i in range(1, len(available)):
                if available[i][0] < min_i and visited[available[i][0]][available[i][1]] <= min_distance :
                    min_i = available[i][0]
                    min_j = available[i][1]
                elif available[i][0] == min_i and visited[available[i][0]][available[i][1]] <= min_distance :
                    if available[i][1] < min_j:
                        min_j = available[i][1]
            queue = [[min_i, min_j]]
            available = []
            second = visited[min_i][min_j]
            visited = init_visited(min_i, min_j, second)
            ate += 1
            if ate == shark:
                ate = 0
                shark += 1
            water[min_i][min_j] = 0
            flag = True
        while queue:
            flag = True
            ti, tj = queue.pop(0)
            for di, dj in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
                ni, nj = ti + di, tj + dj
                if 0 <= ni < N and 0 <= nj < N and water[ni][nj] <= shark and visited[ni][nj] == 0:
                    if water[ni][nj] == shark or water[ni][nj] == 0:
                        queue.append([ni, nj])
                    elif 0 < water[ni][nj] < shark:
                        available.append([ni, nj])
                    visited[ni][nj] = visited[ti][tj] + 1

    return second


def init_visited(ti, tj, s):
    new_visited = [[0] * N for _ in range(N)]
    new_visited[ti][tj] = s
    return new_visited


N = int(input())
water = [list(map(int, input().split())) for _ in range(N)]
si, sj = 0, 0
for i in range(N):
    for j in range(N):
        if water[i][j] == 9:
            si, sj = i, j
            water[i][j] = 0

seconds = bfs(si, sj)
print(seconds)
