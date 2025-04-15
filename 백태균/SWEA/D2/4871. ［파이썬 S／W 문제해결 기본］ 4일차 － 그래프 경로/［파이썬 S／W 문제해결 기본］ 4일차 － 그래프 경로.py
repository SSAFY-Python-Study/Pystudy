# dfs
def dfs(node):
    if visited[node] == 0:
        visited[node] = 1

    for next_node in adj_list[node]:
        visited[next_node] = 1
        dfs(next_node)


T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_list = [[] for _ in range(V+1)]
    visited = [0] * (V+1)

    for i in range(E):
        s, e = map(int, input().split())
        adj_list[s].append(e)

    start, end = map(int, input().split())

    dfs(start)

    if visited[end] == 1:
        print(f'#{tc} 1')

    else:
        print(f'#{tc} 0')
