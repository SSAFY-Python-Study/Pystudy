from collections import deque

def bfs():
    dq = deque([(1, 1)])
    visited = [[-1] * 16 for _ in range(16)]
    # 시작점(1, 1) 방문 표시
    visited[1][1] = 0
    while dq:
        # 디큐
        i, j = dq.popleft()
        if arr[i][j] == "3":
            return 1
        # 상하좌우 델타함수 적용
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = i + di, j + dj
            if 0 <= ni < 16 and 0 <= nj < 16 and visited[ni][nj] == -1 and arr[ni][nj] != "1":
                # 인큐
                dq.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1
    return 0

for _ in range(10):
    test_case = int(input())
    arr = [input() for _ in range(16)]
    print(f"#{test_case} {bfs()}")