import sys
sys.stdin = open('4.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    time_lst = list(map(int,input().split()))
    ans = 'Possible'
    cnt = 0

    for i in range(N-1,0,-1):
        for j in range(i):
            if time_lst[j] > time_lst[j+1]:
                time_lst[j],time_lst[j+1] = time_lst[j+1],time_lst[j]

    for time in time_lst:
        bread_cnt = (time // M) * K - cnt
        if bread_cnt != 0:
            cnt += 1
        else:
            ans = 'Impossible'

    print(f'#{tc} {ans}')


