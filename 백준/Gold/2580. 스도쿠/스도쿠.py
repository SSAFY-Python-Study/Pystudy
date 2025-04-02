def is_valid(x, y, num):
    for i in range(9):
        # 같은 열에 있거나, 같은 행에 있을 때
        if arr[x][i] == num or arr[i][y] == num:
            return False
    # 3 x 3 안에 있을 때
    nx, ny = 3 * (x // 3), 3 * (y // 3)
    for i in range(3):
        for j in range(3):
            if arr[nx + i][ny + j] == num:
                return False
    return True

def recur(cnt):
    global is_completed
    # 정답을 이미 찾았으면
    if is_completed:
        return
    # 빈칸의 수만큼 재귀가 진행되면 종료
    if cnt == len(blanks):
        for i in range(9):
            print(*arr[i])
        is_completed = True
        return
    i, j = blanks[cnt]
    for k in range(1, 10):
        if is_valid(i, j, k):
            arr[i][j] = k
            recur(cnt + 1)
            arr[i][j] = 0

arr = [list(map(int, input().split())) for _ in range(9)]
# 빈칸의 좌표가 들어있는 리스트
blanks = [(i, j) for i in range(9) for j in range(9) if arr[i][j] == 0]
# 재귀 종료 플래그
is_completed = False
recur(0)
