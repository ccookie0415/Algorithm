import sys
sys.stdin = open('부분수열의합.txt','r')

def find(n,sum_):
    global ans

    if n >= N:
        return

    if sum_+A[n] == K:
        ans += 1

    find(n+1, sum_+A[n])
    find(n+1, sum_)

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0

    find(0,0)
    print(f'#{tc} {ans}')