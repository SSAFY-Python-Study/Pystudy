N = int(input())

line = 1
while N > 0:
    N -= line
    line += 1

line -= 1
if line % 2 == 0:
    print(f'{N+line}/{1-N}')
else:
    print(f'{1-N}/{N+line}')