import sys
sys.stdin = open('Magnetic.txt','r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    current = 0
    total = 0

    for j in range(N):
        cnt = 0
        current = 0
        for i in range(N):
            if current == 0 and arr[i][j] == 1:
                cnt += 1
                current = 1
            elif current == 1:
                if arr[i][j] == 1:
                    cnt += 1
                elif arr[i][j] == 2:
                    cnt += 1
                    current = 2
            elif current == 2:
                if arr[i][j] == 2:
                    cnt += 1
        if current == 2:
            total += cnt

    print(f'#{tc} {total}')