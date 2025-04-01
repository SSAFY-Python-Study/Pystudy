N = int(input())
tt = [list(map(int, input().split())) for _ in range(N)]
tt.sort(key=lambda x: (x[1], x[0])) # 종료, 시작 순으로 정렬

ans = 0     # 회의 수 초기화
last = 0    # 처음 끝난 시간 초기화
# 타임테이블 안 시작-종료 시간 순회
for s, e in tt:
    if s >= last:   # 시작 시간이 더 크다면
        ans += 1    # 회의 증가
        last = e    # 마지막 시간 변경
print(ans)