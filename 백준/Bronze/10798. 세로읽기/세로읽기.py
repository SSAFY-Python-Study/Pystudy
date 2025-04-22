arr = [list(map(str, input())) for _ in range(5)]
arr2 = []

for i in range(15):
    temp = []
    for j in range(5):
        if i < len(arr[j]):  # 글자가 있는 경우에만
            temp.append(arr[j][i])
    arr2.append(temp)

for i in range(len(arr2)):
    for j in range(len(arr2[i])):
        print(arr2[i][j], end="")
