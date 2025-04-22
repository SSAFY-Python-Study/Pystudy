# from collections import deque
#
# N = int(input())
# T = int(input())
# hands = list(map(int, input().split()))
# commands = list(map(int, input().split()))
#
#
# for c in range(len(commands)):
#     for _ in range(commands[c]):
#         commands[c]-=1
#         if commands[c] > 0 and len(hands)==0:
#             hands.append(hands)
#         i = hands.popleft()
#     if commands[c] ==0:
#         print(i)

from collections import deque

# 입력 받기
N = int(input())  # 참가자 수
T = int(input())  # 게임 수
hands = list(map(int, input().split()))  # 각 손의 주인 번호
calls = list(map(int, input().split()))  # 각 게임에서 외치는 숫자

# 손들을 deque으로 관리
hands_queue = deque(hands)
results = []

for game in range(T):
    call = calls[game]

    # 외친 숫자-1만큼 맨 아래 손을 위로 올림
    for _ in range(call - 1):
        bottom_hand = hands_queue.popleft()
        hands_queue.append(bottom_hand)

    # call번째 손이 탈락 (맨 아래 손)
    eliminated = hands_queue[0]
    results.append(eliminated)

    # 다음 게임은 탈락한 손의 위치에서 시작하므로
    # 탈락한 손은 그대로 두고 다음 게임 준비
    # (아무 작업 없이 다음 게임으로 넘어감)

# 결과 출력
print(" ".join(map(str, results)))

