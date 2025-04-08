N = int(input())    # 단어의 개수

for i in range(N):
    tmp = []
    arr = input()
    for j in arr:
        if j not in tmp:
            tmp.append(j)
        else:
            if tmp[-1] != j:
                N -= 1
                break

print(N)