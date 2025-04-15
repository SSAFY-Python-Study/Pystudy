N = int(input())
arr = [input() for _ in range(N)]
# print(arr)

ans = list(set(arr))    # 중복 제거
ans.sort()      # 알파벳 순서 정렬
ans.sort(key=len)   # 문자열 길이 기준 정렬

for i in ans:
    print(i)
