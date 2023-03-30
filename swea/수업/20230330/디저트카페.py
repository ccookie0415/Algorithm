import sys
sys.stdin = open('디저트카페.txt','r')

di = [-1,1,1,-1]
dj = [1,1,-1,-1]

def find(ni,nj,k,check):
    global ans,i,j

    if k == 3 and ni == i and nj == j:
        if ans < len(check):
            ans = len(check)
            return

    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in check:
        check = check + [arr[ni][nj]]

    # 직진
        nni = ni + di[k]
        nnj = nj + dj[k]
        find(nni,nnj,k,check)
    
    # 꺾음

        if k < 3:
            nni = ni + di[k+1]
            nnj = nj + dj[k+1]
            find(nni,nnj,k+1,check)

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = -1

    for i in range(1,N):
        for j in range(N):
            check = []
            find(i,j,0,check)

    print(f'#{tc} {ans}')