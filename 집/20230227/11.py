import sys
sys.stdin = open('고기잡이.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = 4*(K-1)

    max_ = 0
    for i in range(N-K+1):
        for j in range(M-K+1):
            x = i
            y = j
            a = 0
            total = arr[i][j]
            for k in range(1,A):
                ni = x + di[a]
                nj = y + dj[a]
                x = ni
                y = nj

                if 0 <= ni < N and 0 <= nj < M:
                    total += arr[ni][nj]

                if k % (K-1) == 0:
                    a += 1

            if max_ < total:
                max_ = total

    print(f'#{tc} {max_}')

