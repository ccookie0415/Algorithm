import sys
sys.stdin = open('이진수2.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = float(input())
    ans = []
    a = 1

    while True:
        if N > 0:
            break

    while True:
        if N <= 0:
            break

        if len(ans) > 12:
            ans = 'overflow'
            break

        ans.append(int(N//2 **(-1*a)))
        N = N % (2 ** (-1 * a))
        a += 1

    print(f'#{tc}',''.join(map(str,ans)))