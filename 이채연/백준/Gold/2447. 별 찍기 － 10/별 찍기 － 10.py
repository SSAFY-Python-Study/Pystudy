# 별 찍기 - 10

def recur(n): # 찍고
    if n == 1:
        return ['*']
    star = recur(n//3)

    stars = []
    for i in star:
        stars.append(i*3)
    for j in star:
        stars.append(j+' '*(n//3)+j)
    for k in star:
        stars.append(k*3)

    return stars

N = int(input())  # n은 3의 거듭제곱
# NxN
print('\n'.join(recur(N)))