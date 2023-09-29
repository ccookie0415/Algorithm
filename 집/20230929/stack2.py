def dfs(n,sum_):
    global ans

    if n == N:
        if sum_ == K:
            ans += 1
        return

    dfs(n+1, sum_ + lst[n])
    dfs(n+1, sum_)


T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    lst = list(map(int,input().split()))
    ans = 0

    dfs(0,0)
    print(f'#{tc} {ans}')