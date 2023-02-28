import sys
sys.stdin = open('Magnetic.txt','r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    cnt = [0] * 100

    for j in range(N):
        for i in range(N):
            if arr[i][j] == 2:
                cnt += 1



