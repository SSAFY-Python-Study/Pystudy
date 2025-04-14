from collections import deque
N = int(input())    # 1~N 참가자
T = int(input())    # 아파트 게임 횟수
apart = list(map(int, input().split()))
nums = list(map(int, input().split()))

d = deque(apart)
defeat = []

for num in nums:
    for _ in range(num-1):
        next = d.popleft()
        d.append(next)
    defeat.append(d[0])

print(*defeat)