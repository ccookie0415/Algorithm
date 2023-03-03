# import sys
# sys.stdin = open('백만장자프로젝트.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))[::-1]
    max_ = 0
    total = 0

    for i in range(N):
        if data[i] > max_:
            max_ = data[i]
        else:
            total += max_ - data[i]

    print(f'#{tc} {total}')