import sys
sys.stdin = open('암호생성기.txt', 'r')

T = 10

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int,input().split()))
    break_ = 0

    while True:
        if break_ == 1:
            break
        for i in range(1, 6):
            n = data.pop(0)
            if n - i <= 0:
                data.append(0)
                break_ = 1
                break
            data.append(n - i)

    print(f'#{tc}', *data)





