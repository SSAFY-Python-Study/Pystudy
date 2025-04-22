arr = input()
stack = []
stick = 0

for i in range(len(arr)):
    if arr[i] == '(':  # 열린 괄호 = 막대기 or 레이저
        stack.append('(')

    else:   # 닫는 괄호 일때
        if arr[i-1]=='(':  # 직전이 여는 괄호다? -> 레이저
            stack.pop() #pop
            stick += len(stack) # 스택 길이 = 막대기 수만큼 더하기
        else:
            stack.pop() #pop
            stick += 1
print(stick)