def possible(channel):
    for ch in str(channel):
        if int(ch) in broken:
            return False
    return True

N = int(input()) # 채널 N
M = int(input()) # 고장난 버튼 수
if M:
    broken = list(map(int, input().split()))
else:
    broken = []

min_press = abs(N-100) # +, - 만 사용했을 때

for num in range(1000001): # 500000 까지 있지만 누를수 있는게 없다면? N보다 클 수 있기 때문에 넉넉잡아 ㄱ
    if possible(num): # 5455라면.. 전부 누를 수 있을때만 TRUE 
        press = len(str(num)) + abs(N-num) # 4번으로 입력하고, 나머지는 N과의 차이만큼 +나 -
        min_press = min(min_press, press) # 1000001까지 중 가장 작은 값으로 갱신됨

print(min_press)