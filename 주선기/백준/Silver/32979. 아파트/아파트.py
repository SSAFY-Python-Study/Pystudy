from collections import deque

N = int(input())
T = int(input())
# deque 초기 값 설정
dq = deque(map(int, input().split()))
arr = list(map(int, input().split()))
losers = []
# 게임 횟수만큼 반복
for item in arr:
    for _ in range(item - 1):
        # 맨 아랫 손 맨 위로 옮겨주기
        dq.rotate(-1)
    # 패배자 리스트에 맨 아랫손 제거
    losers.append(dq[0])
print(*losers)