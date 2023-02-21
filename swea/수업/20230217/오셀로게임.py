import sys
sys.stdin = open('오셀로게임.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[0] * N for _ in range(N)]
    data = [list(input().split()) for _ in range(M)]
    K = int(N/2)

    for i in range(K-1, K+1):
        print(i)
        for j in range(K-1, K+1):
            if i==j:
                arr[i][j] = 2
            else:
                arr[i][j] = 1


    # for i in range(M):
    #     print(data[i])
    #     if data[i][2] == 1:
    #
    #     elif data[i][2] == 2:


