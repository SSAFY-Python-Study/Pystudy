N = int(input())
stack = []
for _ in range(N):
	command = input()
	if command == "top":
		if len(stack) == 0:
			print(-1)
		else:
			print(stack[-1])
	elif command == "empty":
		if len(stack) == 0:
			print(1)
		else:
			print(0)
	elif command == "size":
		print(len(stack))
	elif command == "pop":
		if len(stack) == 0:
			print(-1)
		else:
			print(stack.pop())
	else:
		a, b = command.split()
		stack.append(b)