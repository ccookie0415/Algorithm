import sys
sys.stdin = open('거듭제곱.txt', 'r')

T = 10

def ans(N,M):
    if M == 0:
        return 1
    else:
        return N * ans(N,M-1)

for tc in range(1,T+1):
    tc_num = int(input())
    N,M = map(int,input().split())


    print(f'#{tc} {ans(N,M)}')