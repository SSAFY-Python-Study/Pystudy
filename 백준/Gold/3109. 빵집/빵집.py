import sys
input = sys.stdin.readline

def DFS(si, sj):
    stack = []

    ti, tj = si, sj
    while True:
        if tj == C-1:
            return 1
        for di, dj in [[-1,1],[0,1],[1,1]]:
            ni, nj = ti+di, tj+dj
            if 0 <= ni < R and 0<= nj < C and visited[ni][nj] == 0 and ground[ni][nj] =='.':
                stack.append([ti,tj])
                visited[ni][nj] = 1
                ti, tj = ni, nj
                break
        else:
            if stack:
                # visited[ti][tj] = 0
                ti, tj = stack.pop()
            else:
                break
    return 0


R, C = map(int, input().split())

ground = [list(input().strip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
result = 0
for i in range(R):
    if ground[i][0] == '.':
        result += DFS(i,0)
print(result)