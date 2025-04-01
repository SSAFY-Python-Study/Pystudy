# 조합을 재귀돌려서 M을 넘지 않는 가장 큰 값 리턴하기
def solve(cnt, now, s):     # 개수 / 현재 값 / 합
    global ans
    # 가지치기
    if s > M:
        return
    # 기저조건(종료)
    if cnt == 3:    # 3개를 뽑았을 때
        if s <= M:  # M보다 작거나 같다면
            ans = max(ans, s)   # 그것이 바로 답
            return
        return

    for i in range(now, N):
        p.append(card[i])
        solve(cnt+1, i+1, s+card[i])
        p.pop()


N, M = map(int, input().split())
card = list(map(int, input().split()))
p = []  # 새로운 조합을 넣어줄 리스트
ans = 0     # 정답(최댓값) 초기화

solve(0, 0, 0)
print(ans)