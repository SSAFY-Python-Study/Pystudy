def sum_hi(a,b):
    return a+b

while True:
    A, B = map(int, input().split())
    if A==B==0:
        break
    else:
        result = sum_hi(A,B)
        print(result)