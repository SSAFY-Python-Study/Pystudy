arr = [int(input()) for _ in range(9)]
arr.sort()
# print(arr)
liar = []

find = False
for i in range(8):
    for j in range(i+1, 9):
        if sum(arr)-arr[i]-arr[j] == 100:
            liar += arr[i], arr[j]
            find = True
            break
    if find:
        break

for a in arr:
    if a not in liar:
        print(a)

