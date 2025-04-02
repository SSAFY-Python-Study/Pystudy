def laser(i, j, N):
    global cnt
    for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
        for c in range(N):
            ni, nj = i + di * c, j + dj * c
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] == 1:
                    break
                if arr[ni][nj] == 0:
                    cnt -= 1
    return cnt
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
 
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 0:
                cnt += 1
            if arr[i][j] == 2:
                mi, mj = i, j
                laser(mi, mj, N)
 
    print(f'#{tc} {cnt}')