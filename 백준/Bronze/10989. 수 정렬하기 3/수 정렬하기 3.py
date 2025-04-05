import sys
input = sys.stdin.readline

# 그냥 sorted 쓰면 메모리 초과 -> count 배열 만들어서 정렬해보자!
n = int(input())
num = [0] * (10000 + 1)  # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

for _ in range(n):
    num[int(input())] += 1

for i in range(len(num)):
    for _ in range(num[i]):
        print(i)
