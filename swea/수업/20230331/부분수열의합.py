import sys
sys.stdin = open('부분수열의합.txt','r')

def find(n, total):
    global ans

    if n == N:
        if total == K:
            ans += 1
        return

    find(n+1, total + A[n])
    find(n+1, total)

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    ans = 0

    find(0,0)
    print(f'#{tc} {ans}')