# import sys
# sys.stdin = open('농작물수확.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input())) for _ in range(N)]
    total = 0
    a = 0

    for i in range(N):
        for j in range(N//2-a,N//2+a+1):
            total += arr[i][j]
        if i < N//2:
            a += 1
        else:
            a -= 1
    print(f'#{tc} {total}')
