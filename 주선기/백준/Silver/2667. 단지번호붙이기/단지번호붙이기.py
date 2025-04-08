def recur(x, y):
    # 방문 표시
    visited[x][y] = True
    # 해당 지점부터 단지 갯수 세기
    cnt = 1
    # 상하좌우 순서로 검색
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        nx, ny = x + dx, y + dy
        # 인덱스 안 벗어나고, 방문하지 않았고, 해당 지점 값이 "1"일 때
        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] is False and arr[nx][ny] == "1":
            cnt += recur(nx, ny)
    return cnt

N = int(input())
arr = [input() for _ in range(N)]

# 방문 표시를 위한 visited
visited = [[False] * N for _ in range(N)]
# 아파트 단지를 담을 리스트
complex_list = []

for i in range(N):
    for j in range(N):
        if visited[i][j] is False and arr[i][j] == "1":
            complex_list.append(recur(i, j))
complex_list.sort()

print(len(complex_list))
for complex in complex_list:
    print(complex)