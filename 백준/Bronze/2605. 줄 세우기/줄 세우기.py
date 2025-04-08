from collections import deque

N = int(input())
arr = list(map(int, input().split()))

row = deque()

for i in range(N):
    if i == 0:
        row.append(i+1)

    elif i == 1:
        if arr[i] == 0:
            row.append(i+1)
        elif arr[i] == 1:
            row.appendleft(i+1)

    elif i >= 2:
        row.insert(i-arr[i], i+1)

print(*row)
