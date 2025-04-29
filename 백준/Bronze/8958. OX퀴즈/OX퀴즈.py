T = int(input())

for tc in range(1, T+1):
    arr = input()
    # print(arr)
    s = 0
    ans = 0
    for i in range(len(arr)):
        if arr[i] == 'O':
            s += 1
        else:
            s = 0
        ans += s

    print(ans)


