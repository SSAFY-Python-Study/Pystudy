from collections import deque

q = deque()

N, M = map(int, input().split())
arr = list(map(int, input().split()))

for i in range(1, N+1):
    q.append(i)

cnt = 0

for x in arr:

    while True:
        q_list = list(q)

        if len(q_list) == 1:
            q.popleft()
            break

        mid = len(q) // 2
        left = q_list[:mid+1]
        right = q_list[mid+1:]

        if x in left:
            if x == q_list[0]:
                q.popleft()
                break
            else:
                q.append(q.popleft())
                cnt += 1
        elif x in right:
            q.appendleft(q.pop())
            cnt += 1


print(cnt)



