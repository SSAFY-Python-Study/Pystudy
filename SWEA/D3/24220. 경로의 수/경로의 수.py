def dfs(v):
    global ans
    if v == G:
        ans += 1
        return

    for w in graph[v]:
        if visited[w] == 0:
            visited[w] = 1
            dfs(w)
            visited[w] = 0


T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    e_arr = list(map(int, input().split()))
    graph = [[] for _ in range(N + 1)]

    for e in range(0, E):
        graph[e_arr[e*2]].append(e_arr[e*2 + 1])
    S, G = map(int, input().split())

    ans = 0
    visited = [0] * (N + 1)
    dfs(S)

    print(f'#{tc} {ans}')