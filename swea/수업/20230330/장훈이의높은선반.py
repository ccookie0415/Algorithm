def find(n, total):
    global ans

    if n == N:
        if total >= B:
            ans = min(ans, total)
        return

    find(n+1, total + H[n])
    find(n+1, total)

T = int(input())

for tc in range(1,T+1):
    N,B = map(int,input().split())
    H = list(map(int,input().split()))
    ans = 999999999

    find(0,0)
    print(f'#{tc} {ans-B}')