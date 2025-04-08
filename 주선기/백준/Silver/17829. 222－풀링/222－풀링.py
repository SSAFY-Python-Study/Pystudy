def recur(arr):
    n = len(arr)
    # 풀링이 끝나서 리스트에 요소가 하나만 남았을 때
    if n == 1:
        return arr[0][0]
    # 한 번의 풀링이 끝난 후의 리스트
    new_arr = []
    for i in range(0, n, 2):
        # 한 번의 풀링이 끝난 후의 한 줄 리스트
        row = []
        for j in range(0, n, 2):
            temporary_arr = [
                arr[i][j],
                arr[i][j + 1],
                arr[i + 1][j],
                arr[i + 1][j + 1],
            ]
            temporary_arr.sort()
            # 2번째로 큰 값 추가
            row.append(temporary_arr[2])
        new_arr.append(row)
    return recur(new_arr)

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(recur(arr))