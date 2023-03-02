import sys
sys.stdin = open('두개의숫자열.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    max_ = 0

    if N > M:
        N,M=M,N
        A,B=B,A

    for i in range(M-N+1):
        total = 0
        for j in range(N):
            total += A[j]*B[i+j]

        if max_ < total:
            max_ = total

    print(f'#{tc} {max_}')

