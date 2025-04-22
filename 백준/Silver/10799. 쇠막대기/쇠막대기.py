arr = input()
# print(arr)
stack = []
cnt = 0     # 잘린 쇠막대기 수

for i in range(len(arr)):
    if arr[i] == '(': 
        stack.append(arr[i])
    else: # 닫는 괄호의 경우
        stack.pop()
        if arr[i-1] == '(': 
            cnt += len(stack)
        else: cnt += 1 # 막대의 끝인 경우

print(cnt)