import sys
sys.stdin = open('최소합.txt','r')

di = [0,1]
dj = [1,0]

def find(i,j,total):
    global min_

    if min_ < total:
        return

    if i == N-1 and j == N-1:
        min_ = min(min_, total)
        return

    for k in range(2):
        ni = i + di[k]
        nj = j + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            find(ni,nj,total + arr[ni][nj])


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    min_ = 9999999999

    find(0,0,arr[0][0])
    print(f'#{tc} {min_}')