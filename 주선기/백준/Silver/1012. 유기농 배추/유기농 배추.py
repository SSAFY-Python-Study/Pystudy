from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]
    # 배추 위치 초기화
    for _ in range(K):
        row, col = map(int, input().split())
        arr[col][row] = 1
    # 초기 값 설정
    dq = deque()
    visited = [[False] * M for _ in range(N)]
    cnt = 0
    # arr를 완전 탐색하며 bfs 적용
    for i in range(N):
        for j in range(M):
            # 배추이고, 방문하지 않았을 때
            if arr[i][j] == 1 and not visited[i][j]:
                # bfs 시작
                # 인큐
                dq.append((i, j))
                visited[i][j] = True
                while dq:
                    # 디큐
                    x, y = dq.popleft()
                    # 상하좌우 순서로 델타 함수 적용
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nx, ny = x + dx, y + dy
                        # 인덱스를 벗어나지 않으면
                        if 0 <= nx < N and 0 <= ny < M:
                            # 배추이고, 방문하지 않았으면
                            if arr[nx][ny] == 1 and not visited[nx][ny]:
                                # 인큐
                                dq.append((nx, ny))
                                visited[nx][ny] = True
                # bfs 한 덩어리 끝날 때마다 개수 증가
                cnt += 1
    print(cnt)