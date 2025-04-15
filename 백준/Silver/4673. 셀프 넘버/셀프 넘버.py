# self_number를 찾는 재귀함수
def recur(number):
    next_number = number + sum(map(int, str(number)))
    # 종료 조건
    if next_number > 10000:
        return
    # 이미 셀프 넘버가 아닐 때, 재귀함수 종료
    if not self_number_list[next_number]:
        return
    self_number_list[next_number] = False
    recur(next_number)

# self_number_list를 수정할 함수
def find_self_number():
    for i in range(1, 10001):
        if self_number_list[i]:
            recur(i)

# self_number인지, 아닌지를 저장할 리스트
self_number_list = [True] * 10001
find_self_number()
for i in range(1, 10001):
    if self_number_list[i]:
        print(i)