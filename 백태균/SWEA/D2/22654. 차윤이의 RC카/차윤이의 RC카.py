def find_car():
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                return i, j


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    answer = []

    M = int(input())
    for i in range(M):
        x, y = find_car()
        start_dir = 3
        commands = list(input().split())

        nx = 0
        ny = 0

        for j in range(int(commands[0])):
            command = commands[1][j]

            if command == 'R':
                start_dir = (start_dir + 1) % 4
                nx = dx[start_dir]
                ny = dy[start_dir]

            elif command == 'L':
                start_dir = (start_dir - 1) % 4
                nx = dx[start_dir]
                ny = dy[start_dir]

            elif command == 'A':
                x += nx
                y += ny
                if arr[x][y] == 'T' or x < 0 or x >= N or y < 0 or y >= N:
                    x -= nx
                    y -= ny

        if arr[x][y] == 'Y':
            answer.append(1)
        else:
            answer.append(0)

    print(f'#{tc}', *answer)