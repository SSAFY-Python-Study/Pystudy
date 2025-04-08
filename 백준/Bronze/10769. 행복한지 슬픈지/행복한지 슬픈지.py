# 임티
string = input()

cnt1 = string.count(':-)')
cnt2 = string.count(':-(')

if cnt1 == 0 and cnt2 == 0:
    print('none')
elif cnt1 > cnt2:
    print('happy')
elif cnt1 < cnt2:
    print('sad')
else:
    print('unsure')
