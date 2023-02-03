# (M - N) +1 번 반복

import sys
sys.stdin = open('input_두개의숫자열.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N,M =map(int, input().split())

    A = list(map(int,input().split()))
    B = list(map(int,input().split()))

    if N > M:
        N,M = M,N
        A,B = B,A

    max_sum = 0

    for i in range(M-N+1):
        tmp = 0

        for j in range(N):
            tmp += A[j] * B[j+i]

        if tmp > max_sum:
            max_sum = tmp

    print(f'#{tc} {max_sum}')