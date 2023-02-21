import sys
sys.stdin = open('algo1_sample_in.txt', 'r')

di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    lst = []

    for i in range(1,N-1):
        for j in range(1,N-1):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if arr[i][j] > arr[ni][nj]:
                    cnt += 1
            if cnt == 8:
                lst.append(arr[i][j])


    if len(lst) == 1 or len(lst) == 0:
        ans = -1
    else:
        ans = max(lst) - min(lst)

    print(f'#{tc} {ans}')