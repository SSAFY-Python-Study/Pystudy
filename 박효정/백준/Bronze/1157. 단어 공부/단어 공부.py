string = input().upper() # 전부 대문자로 바꾼다
alpha = {} # 딕셔너리에 알파벳과 등장 순서를 넣을 것!

# 문자열을 순회하며 딕셔너리에 존재하는지 여부를 확인한다
for s in string:
    if alpha.get(s): # 이미 딕셔너리에 있다면 개수(value)를 추가
        alpha[s] += 1
    else: # 아직 없는 알파벳이면 key:1 새로 추가
        alpha[s] = 1

# 등장 횟수가 가장 많은 값을 찾는다
max_num = max(alpha.values())

# 등장 알파벳을 순서대로 넣은 리스트 / ['M', 'I', 'S', 'P']
alpha_list = list(alpha.keys())
# 등장 알파벳의 순서대로 개수를 넣은 리스트 / [1, 4, 4, 1]
num_list = list(alpha.values())

# num_list를 돌며 등장 횟수가 가장 많은 값과 일치하는 인덱스를 구한다
cnt = 0 # 일치하는 개수
idx = -1 # 일치하는 인덱스
result = '' # 등장 횟수가 가장 많은 알파벳
for i in range(len(num_list)):
    if num_list[i] == max_num:
        cnt += 1
        idx = i
    if cnt > 1: # 가장 많이 사용된 알파벳이 1개 이상이라면
        idx = -1
        break

# 가장 많이 사용된 알파벳 출력        
if idx == -1: # 가장 많이 사용된 알파벳이 1개 이상이라면
    print('?')
else:
    print(alpha_list[idx])
