# 100x100 인 visited 행렬을 만들자
visited = [[0]*101 for _ in range(101)]
N = int(input()) # 색종이 개수

area = 0
for _ in range(N):
    x, y = map(int, input().split()) # 각 색종이의 시작 x

    for i in range(10): # 가로세로 변길이 만큼
        for j in range(10):
            if visited[x+i][y+j]==0:
                visited[x+i][y+j] = 1

for i in range(101):
    for j in range(101):
        if visited[i][j]==1:
            area+=1

print(area)