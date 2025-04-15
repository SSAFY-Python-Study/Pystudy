import copy

def eat(li):
    max_cnt = 0

    # 가로 탐색
    for i in range(N):
        j = 0
        cnt = 1
        while True:
            if j == N-1:
                break
            if li[i][j] == li[i][j+1]:
                cnt += 1
                j += 1
            else:
                cnt = 1
                j += 1
                continue
            if max_cnt < cnt:
                max_cnt = cnt

    # 세로 탐색
    for j in range(N):
        i = 0
        cnt = 1
        while True:
            if i == N-1:
                break
            if li[i][j] == li[i+1][j]:
                cnt += 1
                i += 1
            else:
                cnt = 1
                i += 1
                continue
            if max_cnt < cnt:
                max_cnt = cnt

    return max_cnt

N = int(input()) # 보드의 크기
board = [list(input()) for _ in range(N)]
candies = []
result = 0

# 1. candies에 색 바꿀 사탕 좌표 넣기
# 가로 탐색
for i in range(N):
    for j in range(N-1):
        if board[i][j] != board[i][j+1]:
            candies.append([[i,j], [i, j+1]])

# 세로 탐색
for j in range(N):
    for i in range(N-1):
        if board[i][j] != board[i+1][j]:
            candies.append([[i,j], [i+1,j]])


# 사탕구하기
for a, b in candies:
    i, j = a[0], a[1]
    ni, nj = b[0], b[1]
    arr = copy.deepcopy(board)
    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
    if eat(arr) > result:
        result = eat(arr)

print(result)