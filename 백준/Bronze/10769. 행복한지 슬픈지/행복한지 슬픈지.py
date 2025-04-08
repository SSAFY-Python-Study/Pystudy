text = list(input().rstrip())
g = [':', '-', ')']     # good
b = [':', '-', '(']     # bad

happy = sad = 0     # 행복 / 슬픈 이모티콘 수 초기화
# 순회하며 카운트
for i in range(len(text)):
    if text[i] == ':':  # ':'를 만나면 카운트 시작할게요
        if text[i:i+3] == g[0:3]:
            happy += 1
        elif text[i:i+3] == b[0:3]:
            sad += 1
        else:
            continue
# 카운트 검증 시작
if happy == sad == 0:
    print('none')
elif happy == sad:
    print('unsure')
elif happy > sad:
    print('happy')
else:
    print('sad')