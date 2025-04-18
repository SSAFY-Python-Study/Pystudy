T = int(input())

for tc in range(1, T+1):
    N = int(input())    # 당근의 개수
    arr = list(map(int, input().split()))   # 당근 크기

    arr.sort()
    # print(arr)

    min_diff = N

    for i in range(N-2):    # 소 박스에 먼저 담는다고 생각하면, 빈 상자가 없어야 하니까
        for j in range(i+1, N-1):   # 중 박스의 마지막 인덱스까지
            s = i+1
            m = j+1-(i+1)
            l = N-s-m
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                diff = max(s, m, l) - min(s, m, l)
                if min_diff > diff:
                    min_diff = diff

    if min_diff == N:  # 포장할 수 없는 경우
        min_diff = -1
    print(f'#{tc} {min_diff}')