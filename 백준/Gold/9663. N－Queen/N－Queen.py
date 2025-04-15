# 가로, 세로, 대각선 방향으로 같은 선 상에 있는 말을 공격할 수 있다!
def f(i, N):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if col[j] == 0 and dia1[i + j] == 0 and dia2[i + N - 1 - j] == 0:
                # board[i][j] = 1
                col[j] = 1
                dia1[i + j] = 1
                dia2[i + N - 1 - j] = 1
                f(i + 1, N)
                col[j] = 0
                dia1[i + j] = 0
                dia2[i + N - 1 - j] = 0

N = int(input())

board = [[0] * N for _ in range(N)]
cnt = 0
col = [0] * N
dia1 = [0] * (N * 2 - 1)
dia2 = [0] * (N * 2 - 1)
f(0, N)
print(f'{cnt}')