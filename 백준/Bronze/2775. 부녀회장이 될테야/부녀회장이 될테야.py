T = int(input())
for tc in range(1, T+1):
    k = int(input())    # 층
    n = int(input())    # 호
    people = [i for i in range(1, n+1)] # 0층 1호부터 시작해서 n호까지

    for i in range(1, k+1):
        for j in range(1, n):
            people[j] += people[j-1]
            # print(people)
    print(people[-1])
