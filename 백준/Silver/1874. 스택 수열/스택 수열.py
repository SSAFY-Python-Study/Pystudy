N = int(input())
stack = []
start = 1
ans = []

for _ in range(N):
    end = int(input())
    while start <= end:
        stack.append(start)  # 스택에 하나씩 저장
        ans.append('+')
        start += 1

    if stack[-1] == end:  # stack에 저장된 마지막 숫자가 end랑 같을 경우
        stack.pop()  # 마지막 숫자 꺼내기
        ans.append('-')

    else:  # end랑 다를 경우
        print("NO")     # not 'no'
        break

else:
    for i in ans:
        print(i)
