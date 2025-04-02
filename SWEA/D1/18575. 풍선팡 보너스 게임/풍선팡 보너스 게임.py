T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    nums = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0
    min_v = 10000

    for i in range(N):
        for j in range(N):
            s = nums[i][j] 
            for di, dj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                for c in range(1, N):
                    ni, nj = i + di * c, j + dj * c
                    if 0 <= ni < N and 0 <= nj < N:
                        s += nums[ni][nj]

            if max_v < s:
                max_v = s
            if min_v > s:
                min_v = s

    print(f'#{tc} {max_v - min_v}')