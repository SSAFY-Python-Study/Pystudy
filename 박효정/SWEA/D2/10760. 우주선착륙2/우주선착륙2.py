T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 주변 8방향
    di = [-1, -1, -1, 0, 0, 1, 1, 1]
    dj = [-1, 0, 1, -1, 1, -1, 0, 1]

    result = 0

    for i in range(N):
        for j in range(M):
            cnt = 0
            for dir in range(8):
                ni, nj = i + di[dir], j + dj[dir]
                if 0<= ni <N and 0<= nj <M and arr[ni][nj] < arr[i][j]:
                    cnt += 1
            if cnt >= 4:
                result += 1

    print(f'#{tc} {result}')