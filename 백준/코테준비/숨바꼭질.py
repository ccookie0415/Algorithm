import sys
sys.setrecursionlimit(10**7)

def dfs(cnt,current):
    global ans

    if current == K:
        if ans > cnt:
            ans = cnt
    return

    dfs(cnt + 1, current - 1)
    dfs(cnt + 1, current + 1)
    dfs(cnt + 1, current * 2)


N,K = map(int,input().split())
visited = [[0] * 31]
ans = 99999999

dfs(0,N)

print(ans)

