import sys
sys.stdin = open('장훈이의높은선반.txt', 'r')

def find(n, sum_):
    global ans

    if n >= N:
        return

    if sum_ + S[n] >= B:
        if sum_ + S[n] <= ans:
            ans = sum_ + S[n]

    find(n+1, sum_)
    find(n+1, sum_+S[n])

T = int(input())

for tc in range(1,T+1):
    N,B = map(int,input().split())
    S = list(map(int,input().split()))
    S.sort()
    ans = 99999

    find(0,0)
    print(f'#{tc} {ans-B}')