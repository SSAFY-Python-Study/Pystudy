N = int(input())
ans = 0

for i in range(N):
    stack = []
    word = list(input())
    for j in word:
        if len(stack) == 0:
            stack.append(j)
        elif stack[-1] == j:
            stack.pop(-1)
        else:
            stack.append(j)

    if len(stack) == 0:
        ans += 1

print(ans)
