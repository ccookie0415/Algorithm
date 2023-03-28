def dfs(n, cnt, sum_):
    global ans

    if cnt > CNT:
        return

    if sum_ > K:
        return

    if n == N:
        if cnt == CNT and sum_ == K:
            ans += 1
        return

    dfs(n+1, cnt+1, sum_ + lst[n])
    dfs(n+1, cnt, sum_)

T = int(input())

for tc in range(1,T+1):
    CNT, K = map(int,input().split())
    N = 12
    lst = [i for i in range(1,N+1)]

    ans = 0
    dfs(0,0,0)
    print(f'#{tc} {ans}')