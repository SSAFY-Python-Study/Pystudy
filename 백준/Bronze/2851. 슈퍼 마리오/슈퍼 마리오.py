arr = [int(input()) for _ in range(10)]
# print(arr)

# 버섯 먹으면서 100을 넘으면 마지막으로 먹은 버섯을 뺀 수가 100에 가까운지, 넣는게 가까운지 비교
ans = 0
for i in arr:
    ans += i
    if ans >= 100:
        if ans-100 > 100-(ans-i):
            ans -= i
        break

print(ans)