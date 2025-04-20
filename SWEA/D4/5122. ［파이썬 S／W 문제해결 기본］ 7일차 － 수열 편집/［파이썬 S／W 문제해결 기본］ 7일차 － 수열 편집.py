def solve():
    for i in range(len(cmds)):
        cmd = cmds[i]
        if cmd[0] == "I":
            idx, val = int(cmd[1]), int(cmd[2])
            arr.insert(idx, val)
        elif cmd[0] == "D":
            idx = int(cmd[1])
            arr.pop(idx)
        elif cmd[0] == "C":
            idx, val = int(cmd[1]), int(cmd[2])
            arr[idx] = val
    return arr[L] if 0 <= L < len(arr) else (-1)

T = int(input())
for tc in range(1, T + 1):
    N, M, L = map(int, input().split())
    arr = list(map(int, input().split()))
    cmds = [list(input().split()) for _ in range(M)]
    print(f"#{tc} {solve()}")
