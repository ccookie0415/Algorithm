# 고대 유적
# 구조물 최소 크기 1X2
# 구조물은 1, 빈 땅은 0
import sys
sys.stdin = open('고대유적.txt','r')


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(M)]
    max_ = 0
    max2_ = 0
    ans = 0

    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if max_ < cnt:
                    max_ = cnt
            elif arr[i][j] == 0:
                cnt = 0

    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 1:
                cnt += 1
                if max2_ < cnt:
                    max2_ = cnt
            elif arr[i][j] == 0:
                cnt = 0

    if max_ > max2_:
        ans = max_
    else:
        ans = max2_

    print(f'#{tc} {ans}')