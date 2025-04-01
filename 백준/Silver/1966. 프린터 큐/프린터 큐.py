from collections import deque

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())

    q = deque()

    values = list(map(int, input().split()))
    for value in values:
        q.append(value)

    result = 1  # 인쇄 순서 카운터

    while q:  # 큐가 빌 때 까지 반복
        max_value = max(q)  # 현재 큐에서 최대값
        if q[0] < max_value:  # 첫 번째 문서의 중요도가 최대값이 아니면
            q.append(q.popleft())  # 첫 번째 문서의 중요도를 맨 뒤로 이동

        else:  # 최대값이면
            if M == 0:  # 찾고 있는 값이라면
                break  # 중지
            else:  # 아니면
                q.popleft()  # 맨 앞 값을 pop
                result += 1  # 인쇄 순서 증가

        if M > 0:  # 찾는 문서의 인덱스 업데이트
            M -= 1  # 앞의 문서가 처리되었으므로 인덱스 감소
        else:  # M이 0이었다면 (찾는 문서가 맨 앞이었다면)
            M = len(q) - 1  # 문서가 맨 뒤로 이동했으므로 인덱스를 큐의 맨 뒤로 설정

    print(result)



