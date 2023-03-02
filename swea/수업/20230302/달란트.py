import sys
sys.stdin = open('달란트.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,P = map(int,input().split())
    ans = 1

    for _ in range(P-(N%P)):
        ans *= N//P

    for _ in range(N%P):
        ans *= (N//P)+1

    print(f'#{tc} {ans}')
