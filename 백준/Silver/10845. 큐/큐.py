import sys
from collections import deque

q = deque()

N = int(input())
for i in range(N):
    ele = sys.stdin.readline().split()

    if ele[0] == 'push':
        q.append(int(ele[1]))

    elif ele[0] == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())

    elif ele[0] == 'size':
        print(len(q))

    elif ele[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)

    elif ele[0] == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])

    elif ele[0] == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
