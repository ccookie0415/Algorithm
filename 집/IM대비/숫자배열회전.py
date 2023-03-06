import sys
sys.stdin = open('숫자배열회전.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    arr_90 = [[0] * N for _ in range(N)]
    arr_180 = [[0] * N for _ in range(N)]
    arr_270 = [[0] * N for _ in range(N)]
    ans = []

    for i in range(N):
        for j in range(N):
            arr_90[j][N-i-1] = arr[i][j]

    for i in range(N):
        for j in range(N):
            arr_180[j][N-i-1] = arr_90[i][j]

    for i in range(N):
        for j in range(N):
            arr_270[j][N-i-1] = arr_180[i][j]

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')
        print()