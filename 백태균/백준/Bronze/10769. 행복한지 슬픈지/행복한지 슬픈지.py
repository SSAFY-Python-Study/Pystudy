message = list(input())

smile = 0
sad = 0

for i in range(len(message)):
    if message[i] == ':':
        if i >= len(message):
            break

        else:
            if message[i+1] == '-':
                if message[i+2] == ')':
                    smile += 1
                elif message[i+2] == '(':
                    sad += 1

            else:
                continue


if smile == sad == 0:
    print('none')

elif smile == sad:
    print('unsure')

elif smile > sad:
    print('happy')

elif sad > smile:
    print('sad')