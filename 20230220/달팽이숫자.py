import sys
sys.stdin = open('달팽이숫자.txt','r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [([0] * N) for _ in range(N)]

    i = 0
    j = 0
    a = 0
    for k in range(1,N*N+1):
        arr[i][j] = k
        ni = i + di[a]
        nj = j + dj[a]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            i = ni
            j = nj
        else:
            a = (a+1)%4
            i = i + di[a]
            j = j + dj[a]

    print(arr)
