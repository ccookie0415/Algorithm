import sys

T = int(sys.stdin.readline())

for tc in range(1,T+1):
    N = int(sys.stdin.readline())
    arr = [[0] * 1001 for _ in range(1001)]
    ans = []

    for k in range(1,N+1):
        x,y,width,height = map(int, sys.stdin.readline().split())

        for i in range(y,y+height):
            for j in range(x,x+width):
                arr[i][j] = k

    for k in range(1,N+1):
        cnt = 0
        for i in range(1001):
            for j in range(1001):
                if arr[i][j] == k:
                    cnt += 1
        ans.append(cnt)

    for i in ans:
        print(i)

