def finding_spot(arr):
    cnt = 0
    for i in range(N):
        tmp = 0
        for j in range(N):
            if arr[i][j] == '.':
                tmp += 1
            else:
                if tmp >= 2:
                    cnt += 1
                tmp = 0
        if tmp >= 2:
            cnt += 1
    return cnt


N = int(input())
arr = [list(input()) for _ in range(N)]
arr2 = [[arr[i][j] for i in range(N)] for j in range(N)]

print(finding_spot(arr), finding_spot(arr2))