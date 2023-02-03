import sys
sys.stdin = open('input1.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num = list(map(str,input()))
    num += '0'
    tmp = 0
    cnt = 0

    for i in range(N+1):
        if num[i] == '0':
            if tmp < cnt:
                tmp = cnt
                cnt = 0

        elif num[i] == '1':
            cnt += 1

    print(f'#{tc+1} {tmp}')
