T = int(input())

for tc in range(1, T+1):
    quiz = input()
    o_cnt = 0 # 지금까지 O의 개수
    score = 0 # 누적 점수

    for q in quiz:
        if q == 'O': # 맞았다면
            o_cnt += 1 # 맞은 개수 누적
            score += o_cnt # 점수에 추가
        else: # 틀렸다면
            o_cnt = 0 # 맞은 개수 초기화

    print(score)