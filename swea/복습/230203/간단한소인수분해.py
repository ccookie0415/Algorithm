import sys
sys.stdin = open('간단한소인수분해.txt','r')

T = int(input())

for tc in range(1,T+1):
    num = int(input())
    cnt = [0] * 5

    while True:
        if num == 1:
            break
        elif num % 2 == 0:
            num = num // 2
            cnt[0] += 1
        elif num % 3 == 0:
            num = num // 3
            cnt[1] += 1
        elif num % 5 == 0:
            num = num // 5
            cnt[2] += 1
        elif num % 7 == 0:
            num = num // 7
            cnt[3] += 1
        elif num % 11 == 0:
            num = num // 11
            cnt[4] += 1

    print(f'#{tc}', *cnt)