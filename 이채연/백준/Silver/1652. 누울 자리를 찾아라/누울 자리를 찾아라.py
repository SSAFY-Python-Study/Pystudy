
N = int(input())
arr = [input() for _ in range(N)]

row = col = 0

# 가로 체크
for i in range(N):
    cnt = 0
    for j in range(N):
        if arr[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                row += 1
            cnt = 0
    if cnt >= 2:  # 줄 끝에서 끝난 경우
        row += 1

# 세로 체크
for j in range(N):
    cnt = 0
    for i in range(N):
        if arr[i][j] == '.':
            cnt += 1
        else:
            if cnt >= 2:
                col += 1
            cnt = 0
    if cnt >= 2:
        col += 1

print(row, col)