def click(arr):
    count = 0
    for i in range(1, len(arr)):
        if arr[i] == 'Y':
            for j in range(1, len(arr)):
                if j % i == 0:
                    if arr[j] == 'Y':
                        arr[j] = 'N'
                    else:
                        arr[j] = 'Y'
            count += 1
        if 'Y' not in arr:
            return count
    return -1


bulbs = [0] + list(input())

cnt = 0

if 'Y' not in bulbs:
    cnt = 0
else:
    cnt = click(bulbs)

print(cnt)