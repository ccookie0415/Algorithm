def dfs(n, sum_, cnt):
    global ans

    if n == N:
        if sum_ == K and cnt == CNT:
            ans += 1
        return

    dfs(n+1, sum_+lst[n], cnt + 1)
    dfs(n+1, sum_, cnt)


lst = [n for n in range(1,13)]

T = int(input())

for tc in range(1,T+1):
    CNT,K = map(int,input().split())
    N = 12

    ans = 0
    dfs(0,0,0)
    print(f'#{tc} {ans}')