A, B, V = map(int, input().split()) 
# 올라가야 할 거리= V-B
# 한 번에 올라갈 수 있는 거리= A-B

# 정상까지 도달한 경우
if (V-B) % (A-B) == 0:
    print((V-B) //(A-B))
# 정상에 도달하지 못해 미끄러지는 경우
else:
    print(((V-B) // (A-B)) + 1)
