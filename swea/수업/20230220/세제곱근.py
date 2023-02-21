import sys
sys.stdin = open('세제곱근.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    if round(N**(1/3))**3 == N:
        ans = round(N**(1/3))
    else:
        ans = -1

    print(f'#{tc} {ans}')

