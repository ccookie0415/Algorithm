import sys
sys.stdin = open('input_어디에단어가.txt', 'r')


T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    total = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            total += 1


    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    total += 1
                cnt = 0
            else :
                cnt += 1
        if cnt == K:
            total += 1

    print(f'#{tc} {total}')