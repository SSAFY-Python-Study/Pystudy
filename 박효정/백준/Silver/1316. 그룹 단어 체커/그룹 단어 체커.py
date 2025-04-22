N = int(input()) # 3
arr = [input() for _ in range(N)] # happy, new, year
cnt = 0
for string in arr: # 3개 단어 확인
    if len(string) == 1:
        cnt += 1
        continue

    words = []

    for i in range(len(string) - 1):
        if string[i] != string[i+1]:
            words.append(string[i])
    if string[-1] in words:
        words.append(string[-1])
    check = set(words)

    if len(check) == len(words):
        cnt += 1

print(cnt)