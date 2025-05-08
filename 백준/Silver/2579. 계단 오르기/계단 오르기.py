N=int(input()) 
s=[int(input()) for _ in range(N)] 
dp=[0]*N
if len(s)<=2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(s))
else: # 계단이 3개 이상일 때
    dp[0]=s[0] # 첫 번째 계단 
    dp[1]=s[0]+s[1] # 두 번째 계단
    for i in range(2, N): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+s[i-1]+s[i], dp[i-2]+s[i])
    print(dp[-1])