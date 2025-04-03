N = int(input())
room = [list(input()) for _ in range(N)]
w = 0   # 가로 누울곳 초기화
l = 0   # 세로 누울곳 초기화

# 가로 탐색
for i in range(N):
    cnt = 0
    for j in range(N):
        if room[i][j] == '.':   # '.'을 만나면 cnt + 1 시작
            cnt += 1
        else:   # 탐색하다가 'X'를 만났다면
            if cnt >= 2:    # cnt>=2인지 검증 후,
                w += 1      # 누울곳 +1,
            cnt = 0  # cnt 초기화
        # 한 행/열이 끝날 때 까지, 다시 탐색 시작('.'만나면 cnt+1)
    if cnt >= 2:    # 한 행을 다 돌았을 때도 검증
        w += 1

# 세로 탐색
for j in range(N):
    cnt = 0
    for i in range(N):
        if room[i][j] == '.':   # '.'을 만나면 cnt + 1 시작
            cnt += 1
        else:   # 탐색하다가 'X'를 만났다면
            if cnt >= 2:    # cnt>=2인지 검증 후,
                l += 1      # 누울곳 +1,
            cnt = 0     # cnt 초기화
        # 한 행/열이 끝날 때 까지, 다시 탐색 시작('.'만나면 cnt+1)
    if cnt >= 2:    # 한 행을 다 돌았을 때도 검증
       l += 1

print(w, l)