import sys
sys.stdin = open('우주선착륙2.txt', 'r')

di = [-1,-1,-1,0,0,1,1,1]
dj = [-1,0,1,-1,1,-1,0,1]

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[9999999] * (M+2)] + [([9999999] + list(map(int,input().split())) + [9999999]) for _ in range(N)] + [[9999999] * (M+2)]
    ans = 0

    # print(arr)
    for i in range(1,N+1):
        for j in range(1, M+1):
            cnt = 0
            for k in range(8):
                ni = i + di[k]
                nj = j + dj[k]
                if arr[ni][nj] < arr[i][j]:
                    cnt += 1
                    if cnt == 4:
                        ans += 1
                        break


    print(f'#{tc} {ans}')

