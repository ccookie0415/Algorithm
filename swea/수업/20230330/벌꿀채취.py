import sys
sys.stdin = open('벌꿀채취.txt','r')

def find(n,cnt,sum_,ci,cj):
    global max_

    if cnt > C:
        return

    if n == M:
        if max_ < sum_:
            max_ = sum_
        return

    find(n+1, cnt+arr[ci][cj+n], sum_+arr[ci][cj+n]**2, ci, cj)
    find(n+1, cnt, sum_, ci, cj)

T = int(input())

for tc in range(1,T+1):
    N,M,C = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N-M+1):
            max_ = 0
            find(0,0,0,i,j)
            sum_1 = max_
            for i_2 in range(i,N):
                if i == i_2:
                    sj = j+M
                else:
                    sj = 0
                for j_2 in range(sj, N-M+1):
                    max_ = 0
                    find(0,0,0,i_2,j_2)
                    ans = max(ans, sum_1+max_)

    print(f'#{tc} {ans}')
