import sys
sys.stdin = open('어디에단어가.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    new_arr = list(zip(*arr))
    ans = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
            if arr[i][j] == 0 or j == N-1:
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if new_arr[i][j] == 1:
                cnt += 1
            if new_arr[i][j] == 0 or j == N - 1:
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
    print(f'#{tc} {ans}')