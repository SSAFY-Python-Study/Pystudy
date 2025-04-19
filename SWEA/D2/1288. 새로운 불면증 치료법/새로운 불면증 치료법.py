def solve():
    my_set = set()
    i = 1
    while True:
        my_str = str(N * i)
        for s in my_str:
            my_set.add(int(s))
        # 0 ~ 9까지 모든 숫자를 봤다면
        if len(my_set) == 10:
            return my_str
        i += 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print(f"#{tc} {solve()}")
