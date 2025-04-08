N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# A만 재배열이 가능하다 -> 상관없이 모두 재배열 가능
# A를 오름차순 정렬하자
a = sorted(A)
# B를 내림차순 정렬하자
b = sorted(B, reverse=True)
ans = 0     # 정답 초기화
for i in range(N):
    ans += a[i]*b[i]

print(ans)