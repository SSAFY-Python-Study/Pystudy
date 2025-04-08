import math
# findset 연산
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

# union 연산
def union(x, y):
    ref_x = parents[x]
    ref_y = parents[y]
    if ref_x == ref_y:
        return
    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


# 입력 받기
N = int(input())
x_list = []
y_list = []
for _ in range(N):
    x, y = map(float, input().split())
    x_list.append(x)
    y_list.append(y)


parents = [i for i in range(N)]     # 부모 배열 만들어 주기(make 연산)
min_cost = 0    # 최솟값 초기화

# 간선 정보를 저장하자
edges = []
for i in range(N):
    for j in range(i+1, N):
        cost = math.sqrt((x_list[j] - x_list[i])**2 + (y_list[j] - y_list[i])**2)
        edges.append((i, j, cost))

# 가중치를 오름차순으로 정렬하자
edges.sort(key=lambda x: x[2])

# 앞에서부터 사이클 유무를 검사하자
cnt = 0
for u, v, w in edges:
    if find_set(u) != find_set(v):  # 대표자가 다르다면
        union(u, v)     # union 연산 해주기
        min_cost += w   # 가중치 더해주고
        cnt += 1        # 간선 개수 증가
    if cnt == N-1:      # 간선이 N-1개가 되면 종료
        break

print(f'{min_cost:.2f}')