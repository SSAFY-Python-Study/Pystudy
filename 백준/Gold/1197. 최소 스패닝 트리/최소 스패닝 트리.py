from heapq import heappush, heappop
import sys
input = sys.stdin.readline

def prim(start, weight):
    visit = [0] * (V + 1) # 정점 방문 처리
    q = [[weight, start]] 
    ans = 0 # 가중치 합
    cnt = 0 # 간선의 개수
    while cnt < V: # 간선의 개수 최대는 V-1
        k, v = heappop(q)
        if visit[v]: continue # 이미 방문한 정점이면 지나감
        visit[v] = 1 
        ans += k 
        cnt += 1 
        for u, w in G[v]: # 해당 정점의 간선정보를 불러옴
            heappush(q, [w, u]) 
    return ans

V, E = map(int, input().split())
G = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append([v, w])
    G[v].append([u, w])

print(prim(1, 0))