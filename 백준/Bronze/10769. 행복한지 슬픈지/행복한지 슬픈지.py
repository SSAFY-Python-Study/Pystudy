my_str = input()
happy_cnt = sad_cnt = 0
for i in range(len(my_str) - 2):
    if my_str[i:i + 3] == ":-)":
        happy_cnt += 1
    if my_str[i:i + 3] == ":-(":
        sad_cnt += 1
if happy_cnt == 0 and sad_cnt == 0:
    print("none")
elif happy_cnt > sad_cnt:
    print("happy")
elif happy_cnt < sad_cnt:
    print("sad")
elif happy_cnt == sad_cnt:
    print("unsure")