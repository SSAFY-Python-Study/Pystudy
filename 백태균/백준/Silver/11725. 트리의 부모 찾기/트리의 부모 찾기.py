import sys
sys.setrecursionlimit(10**6)

def dfs(n):
    for node in adj_list[n]:
        if visited[node] == 0:
            visited[node] = n  # 어떤 노드로부터 방문했는지 저장
            dfs(node)


N = int(sys.stdin.readline())
adj_list = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

dfs(1)

for i in range(2, N+1):
    print(visited[i])