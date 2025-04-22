import sys
input = sys.stdin.readline

from collections import deque

def bfs(n):
    q = deque()
    q.append(n)
    isCycle = False  # 현재 연결 요소에서 사이클 발견 여부를 추적하는 플래그

    while q:  # 큐가 빌 때까지 반복
        x = q.popleft()  # 큐에서 첫 번째 노드를 제거하고 가져옴

        if visited[x] != 0:  # 이미 방문한 노드라면
            isCycle = True  # 사이클을 발견했다는 뜻

        visited[x] = 1  # 현재 노드를 방문 처리

        for node in graph[x]:  # 인접한 모든 노드 탐색
            if visited[node] == 0:  # 인접 노드가 방문되지 않았다면
                q.append(node)  # 큐에 추가

    return isCycle  # 해당 연결 요소에 사이클이 있는지 여부 반환


case = 0
while True:
    case += 1
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)

    for i in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    ans = 0
    for i in range(1, n+1):  # 각 노드 확인
        if visited[i] == 0:  # 노드가 아직 방문되지 않았다면
            if not bfs(i):  # 이 노드에서 BFS 시작
                ans += 1

    if ans == 0:
        print(f'Case {case}: No trees.')
    elif ans == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {ans} trees.')

