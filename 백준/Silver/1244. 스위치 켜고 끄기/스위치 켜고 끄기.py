n = int(input())
switches = [-1] + list(map(int, input().split()))  
k = int(input())
students = []

for _ in range(k):
    x, y = map(int, input().split())
    students.append((x, y))

for x, y in students:
    if x == 1:  # 남학생이라면
        for i in range(y, n + 1, y):  # 받은 수의 배수인 스위치 번호에 대해서
            switches[i] = 1 if switches[i] == 0 else 0

    else:  # 여학생이라면
        check = []
        check.append(y)
        left = len(switches[1:y])  # 대칭의 왼쪽 부분
        right = len(switches[y + 1:])  # 대칭의 오른쪽 부분
        min_len = min(left, right)  # 둘 중에 짧은 부분의 길이 기준

        for i in range(1, min_len + 1):
            if switches[y - i] == switches[y + i]:  # 대칭이라면 append
                check.append(y - i)
                check.append(y + i)
            else:
                break  # 대칭 아니면 break

        # 처음에 여학생이 받은 수를 check에 집어넣으므로
        # 이후 대칭인 게 있다면 1보다 크기가 클 것임
        if len(check) > 1:
            for i in check:
                switches[i] = 1 if switches[i] == 0 else 0

        else:  # check의 길이가 1이라면 처음 양 옆의 스위치가 대칭이 아닐 것임
            switches[y] = 1 if switches[y] == 0 else 0

for i in range(1, n + 1, 20):
    print(*switches[i:i + 20])