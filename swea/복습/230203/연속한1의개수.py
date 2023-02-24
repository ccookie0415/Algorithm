import sys
sys.stdin = open('연속한1의개수.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input()))
    max_ = 0
    cnt = 0

    for i in range(N):
        if lst[i] == 1:
            cnt += 1
            if max_ < cnt:
                max_ = cnt
        else:
            cnt = 0

    print(f'#{tc} {max_}')