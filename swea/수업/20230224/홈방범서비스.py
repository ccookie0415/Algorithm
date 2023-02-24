import sys
sys.stdin = open('홈방범서비스.txt','r')

di = [-1,0,1,0]
dj = [0,-1,0,1]

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    max_ = 0

    for i in range(N):
        for j in range(N):
            cnt = 0
            for K in range(N):
                cost = K * K + (K-1) * (K-1)
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]
                if arr[ni][nj] == 1:
                    cnt += 1

    # for i in range(1,N+1):
    #     K = i
    #     cost = K * K + (K-1)*(K-1)
    #     for j in range(K):
    #         for k in range(4):
    #             ni = i + j*di[k]
    #             nj = i + j*dj[k]




