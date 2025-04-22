from collections import deque

def bfs(node, target):
    q = deque()
    q.append(node)
    visited[node] = 1

    while q:
        v = q.popleft()

        for n_v in adj_list[v]:
            if visited[n_v] == 0:
                visited[n_v] = 1
                distance[n_v] = distance[v] + 1
                q.append(n_v)

                if n_v == target:
                    return distance[n_v]

    return 0  # 연결되어있지 않는 경우

T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)
    distance = [0] * (V+1)

    for _ in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)
        adj_list[e].append(s)

    start, end = map(int, input().split())

    result = bfs(start, end)

    print(f'#{tc} {result}')
