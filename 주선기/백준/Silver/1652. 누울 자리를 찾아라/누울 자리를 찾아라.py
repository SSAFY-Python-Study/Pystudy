N = int(input())
arr = [input() for _ in range(N)]
col_cnt = row_cnt = 0
is_able = True
# 가로 확인
for i in range(N):
    is_able = True
    for j in range(N - 1):
        if is_able and arr[i][j:j + 2] == "..":
            col_cnt += 1
            is_able = False
        if arr[i][j] == "X":
            is_able = True
# 세로 확인
for j in range(N):
    is_able = True
    for i in range(N - 1):
        if is_able and "".join(arr[k][j] for k in range(i, i + 2)) == "..":
            row_cnt += 1
            is_able = False
        if arr[i][j] == "X":
            is_able = True
print(col_cnt, row_cnt)