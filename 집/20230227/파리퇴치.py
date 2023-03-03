import sys
sys.stdin = open('파리퇴치.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    max_ = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            total = 0
            for k in range(i,i+M):
                for l in range(j,j+M):
                    total += arr[k][l]
            if total > max_:
                max_ = total

    print(f'#{tc} {max_}')





