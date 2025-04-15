def dfs(V, N):
    visited = [0]*(N+1)
    stack = []
    ans = []

    while True:
        # 처음 방문한 곳일 때는 방문 표시를 하고 프린트
        if visited[V] == 0:
            visited[V] = 1
            ans.append(V)
        # v에 인접한 w에 대해서, 방문 안했으면 스택에 넣고 w로 이동
        for w in adj_list[V]:
            if visited[w] == 0:
                stack.append(V)
                V = w
                break
        # 더 이상 인접한 정점이 없으면 스택에 값이 있는지 확인해보기
        else:
            # 있으면 빼준다
            if stack:
                V = stack.pop()
            # 없으면 반복 종료
            else:
                break
    return ans


def bfs(V, N):
    visited = [0] * (N+1)
    # 큐를 만들고 시작점 인큐,visited 배열도 업데이트
    q = []
    q.append(V)
    visited[V] = 1
    ans = []

    while q:
        # 큐에서 정점을 하나씩 꺼내서 방문하기
        t = q.pop(0)
        ans.append(t)
        # 현재 정점 t에서 인접한 정점 w가 방문하지 않은 정점이면 큐에 넣고 방문 표시
        for w in adj_list[t]:
            if visited[w] == 0:
                q.append(w)
                visited[w] = 1
    return ans



N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N+1)]
for i in range(M):
    v1, v2 = map(int, input().split())
    adj_list[v1].append(v2)
    adj_list[v2].append(v1)

# 정점 번호가 작은 것부터 방문하게 하기 위해 정렬해야 함
for lst in adj_list:
    lst.sort()

# print(" ".join(map(str, dfs(V, N))))
# print(" ".join(map(str, bfs(V, N))))
print(*dfs(V, N))
print(*bfs(V, N))