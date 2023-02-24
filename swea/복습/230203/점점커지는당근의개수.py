import sys
sys.stdin = open('점점커지는당근의개수.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    carrot = list(map(int,input().split()))
    max_ = 1
    cnt = 1

    for i in range(1,N):
        if carrot[i] > carrot[i-1]:
            cnt += 1
            if max_ < cnt:
                max_ = cnt
        else:
            cnt = 1

    print(f'#{tc} {max_}')