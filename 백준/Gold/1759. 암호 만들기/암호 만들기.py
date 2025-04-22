def back_tracking(cnt, idx):
    # 백트래킹
    if cnt == l:  # 암호 길이가 l이 되면
        v_cnt = 0  # 모음 수
        c_cnt = 0  # 자음 수

        # 모음과 자음 개수 세기
        for x in answer:
            if x in vowels:
                v_cnt += 1
            else:
                c_cnt += 1

        # 조건 확인: 최소 1개 모음, 최소 2개 자음
        if v_cnt >= 1 and c_cnt >= 2:
            print("".join(answer))

        return

    for i in range(idx, c):
        answer.append(arr[i])
        back_tracking(cnt+1, i+1)  # 다음 문자 선택 (재귀 호출)
        answer.pop()  # 백트레킹: 선택한 문자 제거



l, c = map(int, input().split())
arr = list(input().split())
arr.sort()
answer = []
vowels = ['a', 'e', 'i', 'o', 'u']

back_tracking(0, 0)

