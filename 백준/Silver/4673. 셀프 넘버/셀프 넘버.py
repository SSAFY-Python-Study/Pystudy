# 숫자 n을 인자로 받아서 생성자 not_self_num을 반환하는 함수
def finding_self_num(n):
    N = str(n)    # 슬라이싱하기 위해 str으로 바꿈
    not_self_num = 0
    for i in range(len(N)):
        not_self_num += int(N[i])   # 각 자리 수를 더하고
    not_self_num +=  n      # n값도 더하기
    return not_self_num

ans = set() # 중복 제거
for i in range(10000):
    ans.add(finding_self_num(i))

# 1부터 10000까지 생성자 집합 ans에 없으면 self_num  
for j in range(1,10001):
    if j not in ans:
        print(j)
