width, height = map(int, input().split())
n = int(input())

w = [0, width]
h = [0, height]

for _ in range(n):
    a, b = map(int, input().split())

    if a == 1:  # 가로
        w.append(b)
    elif a == 0:  # 세로
        h.append(b)

w.sort()
h.sort()

result = 0
for i in range(len(w) - 1):
    ww = w[i+1] - w[i]
    for j in range(len(h) - 1):
        hh = h[j+1] - h[j]

        wh = ww * hh

        if wh > result:
            result = wh

print(result)