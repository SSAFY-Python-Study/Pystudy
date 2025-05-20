from sys import stdin as s
def bfs(maze, g):
    visited = [[0] * M for _ in range(N)]
    queue = [[0, 0]]
    visited[0][0] = 1
    min_distance = N*M
    while queue:
        ti, tj = queue.pop(0)
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1,0]]:
            ni, nj = ti + di, tj + dj
            if ni == g[0] and nj == g[1]:
                # if visited[ti][tj] + 1 < min_distance:
                #     min_distance = visited[ti][tj] + 1
                # break
                return visited[ti][tj] + 1
            if 0 <= ni < N and 0 <= nj < M and maze[ni][nj] == 1 and visited[ni][nj] == 0:
                queue.append([ni, nj])
                visited[ni][nj] = visited[ti][tj] + 1
                # ti, tj = ni, nj
    return min_distance


input = s.readline
N, M = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

i = j = 0
# 최단 거리 -> bfs
distance = bfs(maze, [N - 1, M - 1])
print(f'{distance}')