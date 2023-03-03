import sys
sys.stdin = open('러시아국기같은깃발.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [input() for _ in range(N)]
    ans = 0

    for white in range(0,N-2):
        for blue in range(white+1,N-1):
            cnt = 0
            for s in range(0,white+1):
                cnt += arr[s].count('W')
            for s in range(white+1,blue+1):
                cnt += arr[s].count('B')
            for s in range(blue+1,N):
                cnt += arr[s].count('R')
            ans = max(ans,cnt)
    print(f'#{tc} {N*M - ans}')
