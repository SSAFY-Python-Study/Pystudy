N = int(input()) # 스위치 개수
arr = list(map(int, input().split()))
S = int(input()) # 학생 수 S
# 1 남, 2 여
for _ in range(S):
    gender, num = map(int, input().split()) # 남녀여부, 숫자
    if gender == 1: # 남학생일 때
        # 스위치 번호가 받은 수의 배수이면, 그 스위치의 상태를 바꾼다
        # num 3이라면
        for i in range(N):
            if (i+1) % num == 0:
                if arr[i] == 1:
                    arr[i] = 0
                elif arr[i] == 0:
                    arr[i] = 1
    elif gender == 2: # 여학생일 때
        # num = 3이면 index상으로는 2
        idx = num-1
        if arr[idx] == 1:
            arr[idx] = 0
        else:
            arr[idx] = 1
        # N//2 만큼 돌자
        for j in range(1, N+1):
            left = idx-j
            right = idx+j
            if 0<= left and right < N:
                if arr[left] == arr[right]:
                    if arr[left] == 1:
                        arr[left] = 0
                        arr[right] = 0
                    elif arr[left] == 0:
                        arr[left] = 1
                        arr[right] = 1
                else:
                    break
            else:
                break

if len(arr) <= 20:
    print(*arr, sep=' ')
else:
    # 몇 번 반복할까?
    cnt = len(arr) // 20

    # 남은개수는?
    cnt_left = len(arr) % 20

    a = 0
    s = 0
    e = 19
    while a <= cnt:
        if e < N:
            print(*arr[s:e+1], sep=' ')
        else:
            print(*arr[s:], sep=' ')
        s += 20
        e += 20
        a += 1