E, S, M = map(int, input().split())

year = e = s = m = 1

# 1부터 시작해서 1씩 카운트
# 넘어갈때마다 빼서 돌려주면서 E, S, M과 일치하는 순간 찾기
while True:
    if E==e and S==s and M==m:
        break
    year, e, s, m = year +1, e+1, s+1, m+1
    if e > 15:
        e -= 15
    if s > 28:
        s -= 28
    if m > 19:
        m -= 19

print(year)