def find(cnt, height, start):
    global result
    if height > 100:
        return

    if cnt == 7:
        if height == 100:
            result.append(sorted(seven[:])) # 바로 append하니까 seven을 참조해서 계속 변함.. 복사할 것
            return
        return

    for i in range(start, 9):
        seven.append(arr[i])
        find(cnt + 1, height + arr[i], i+1)
        seven.pop()

arr = [0] * 9

for i in range(9):
    arr[i] = int(input())

result = []
seven = []

find(0, 0, 0)

for i in range(7):
    print(result[0][i])