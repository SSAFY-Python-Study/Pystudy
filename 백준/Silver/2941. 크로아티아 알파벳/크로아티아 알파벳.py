word = input()

i = 0
cnt = 0
while True:
    if i >= len(word):
        break
    if i == len(word)-1: # 마지막 글자라면
        cnt += 1
        break

    if word[i] == 'c':
        # 바로 옆 글자를 확인한다
        if word[i+1] == '=' or word[i+1] == '-':
            cnt += 1
            i += 2
            continue
    elif word[i] == 'd':
        if word[i+1] == 'z':
            if i+2 == len(word):
                cnt += 2
                break
            if word[i+2] == '=':
                cnt += 1
                i += 3
                continue
            else:
                cnt += 1
                i += 1
                continue

        elif word[i+1] == '-':
            cnt += 1
            i += 2
            continue

    elif word[i] == 'l':
        if word[i+1] == 'j':
            cnt += 1
            i += 2
            continue

    elif word[i] == 'n':
        if word[i+1] == 'j':
            cnt += 1
            i += 2
            continue
    elif word[i] == 's':
        if word[i+1] == '=':
            cnt += 1
            i += 2
            continue
    elif word[i] == 'z':
        if word[i+1] == '=':
            cnt += 1
            i += 2
            continue

    cnt += 1
    i += 1

print(cnt)