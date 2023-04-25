def dfs(n, A_team, B_team):
    global ans

    if n == N:
        if len(A_team) == A and len(B_team) == A:
            value_a = 0
            value_b = 0
            for i in range(A):
                for j in range(A):
                    value_a += arr[A_team[i]][A_team[j]]
                    value_b += arr[B_team[i]][B_team[j]]

            if abs(value_a - value_b) < ans:
                ans = abs(value_a - value_b)
        return

    dfs(n+1, A_team + [n], B_team)
    dfs(n+1, A_team, B_team + [n])

N = int(input())
A = N//2
arr = [list(map(int,input().split())) for _ in range(N)]
ans = 99999999

dfs(0,[],[])
print(ans)




