def find_target(x, y):
    global target

    num = 1
    arr[x][y] = num
    di = 0

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while True:
        if num == target:
            return x+1, y+1

        nx = x + dx[di]
        ny = y + dy[di]

        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] == 0: # 범위 안에 있으면
            num += 1
            arr[nx][ny] = num
            x = nx
            y = ny

        else:
            di = (di + 1) % 4


C, R = map(int, input().split())
arr = [[0] * C for _ in range(R)]

target = int(input())

if target > C * R:
    print(0)
else:
    x, y = find_target(0, 0)
    print(y, x)
