pipes = input()
stack = []
pipe_cnt = 0
for i in range(len(pipes)):
    # 한 쇠막대기의 시작점일 때
    if pipes[i] == "(":
        # push
        stack.append("(")
    else:
        stack.pop()
        # 레이저일 때
        if pipes[i - 1] == "(":
            pipe_cnt += len(stack)
        # 한 쇠막대기의 끝점일 때
        else:
            pipe_cnt += 1
print(pipe_cnt)