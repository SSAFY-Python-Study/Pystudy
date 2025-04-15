N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# print(arr)

arr.sort(key=lambda x: (x[0], x[1]))
# print(arr)
for i in range(N):
    print(arr[i][0], arr[i][1])