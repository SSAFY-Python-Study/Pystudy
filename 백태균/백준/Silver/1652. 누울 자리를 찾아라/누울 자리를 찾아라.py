N = int(input())
arr = [list(input()) for _ in range(N)]

horizontal_cnt = 0
vertical_cnt = 0

for i in range(N):
    horizontal = 0
    for j in range(N):
        if arr[i][j] == '.':
            horizontal += 1
            if horizontal == 2:
                horizontal_cnt += 1
        else:
            horizontal = 0

for j in range(N):
    verticle = 0
    for i in range(N):
        if arr[i][j] == '.':
            verticle += 1
            if verticle == 2:
                vertical_cnt += 1
        else:
            verticle = 0


print(horizontal_cnt, vertical_cnt)
