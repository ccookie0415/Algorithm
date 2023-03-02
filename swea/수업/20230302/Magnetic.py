import sys
sys.stdin = open('Magnetic.txt','r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    current = 0
    total = 0

    for j in range(N):
        current = 0
        for i in range(N):
            if arr[i][j] == 1 and current == 0:
                current = 1
            elif arr[i][j] == 2:
                if current == 1:
                    current = 0
                    total += 1



    print(f'#{tc} {total}')