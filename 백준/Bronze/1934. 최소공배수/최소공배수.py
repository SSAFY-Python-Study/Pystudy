# import math
#
# T = int(input())
# for _ in range(T):
#     a, b = map(int, input().split())
#     print(math.lcm(a, b))

T = int(input())
for _ in range(T):
    lcm = []
    a, b = map(int, input().split())
    
    # 최소공배수 구하는 법: 두 수의 곱을 두 수의 공약수 중 젤 큰 걸로 나누기
    # 평소처럼 소인수분해하면 구현이 너무 어렵다..
    
    for i in range(1, min(a, b)+1):
        if a%i == 0 and b%i == 0:
            lcm.append(i)
    print(a*b//max(lcm))
