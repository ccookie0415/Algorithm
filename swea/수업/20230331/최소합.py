import sys
sys.stdin = open('최소합.txt','r')

di = [0,1]
dj = [1,0]

def find(x,y,total):
    global ans

    if total >= ans:
        return

    if x == N-1 and y == N-1:
        if total < ans:
            ans = total
        return

    for k in range(2):
        ni = x + di[k]
        nj = y + dj[k]
        if 0 <= ni < N and 0 <= nj < N:
            find(ni,nj,total+arr[ni][nj])


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 99999999

    find(0,0,arr[0][0])
    print(f'#{tc} {ans}')
