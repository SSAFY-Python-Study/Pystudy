from collections import deque

N = int(input())    # 참가자 수
T = int(input())    # 아파트 게임의 횟수
arr = list(map(int, input().split()))   # 손의 위치
num = list(map(int, input().split()))   # 교선이가 부르는 수

q = deque()
for a in arr:
    q.append(a)

loser = []

for i in num:
    for j in range(i-1):
        new_turn = q.popleft()
        q.append(new_turn)
    loser.append(q[0])

print(*loser)
