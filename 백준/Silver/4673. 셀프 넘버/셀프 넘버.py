# 1부터 10000까지의 카프레카수 리스트를 만들자
kap = []
for i in range(1, 10001):
    x = i + sum(map(int, str(i)))
    kap.append(x)

for i in range(1, 10001):   # 다시 1부터 10000까지 돌며,
    if i not in kap:
        print(i)    # 해당 값을 출력하자