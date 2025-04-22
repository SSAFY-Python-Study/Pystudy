def solve():
    lastNBit = (1 << N) - 1
    if lastNBit == (M & lastNBit):
        return "ON"
    else:
        return "OFF"

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print(f"#{tc} {solve()}")
