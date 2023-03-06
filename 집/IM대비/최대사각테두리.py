T = int(input())
di = [0,1,0,-1]
dj = [1,0,-1,0]


for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0
    A = (K-1)*4


    for i in range(N-K+1):
        for j in range(M-K+1):
            a = 0
            total = 0
            ni = i
            nj = j
            for k in range(A):
                total += arr[ni][nj]
                if k != 0 and k % (K-1) == 0:
                    a += 1
                    ni = ni + di[a]
                    nj = nj + dj[a]
                else:
                    ni = ni + di[a]
                    nj = nj + dj[a]
            if total > max_:
                max_ = total


    print(f'#{tc} {max_}')