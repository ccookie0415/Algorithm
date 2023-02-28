import sys
sys.stdin = open('농작물수확.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = N//2
    arr = [list(map(int,input())) for _ in range(N)]
    ans = 0
    a = -1

    for i in range(N):
        if i <= A:
            a += 1
        else:
            a -= 1
        for j in range(A-a,A+a+1):
            ans += arr[i][j]
    print(f'#{tc} {ans}')