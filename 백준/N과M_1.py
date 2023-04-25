# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열

def find(n, lst):
    global result

    if n > M:
        return

    if n == M:
        result.append(lst)

    for j in range(1, N + 1):
        if visited[j] == 0:
            visited[j] = 1
            find(n + 1, lst + [j])
            visited[j] = 0


N, M = map(int, input().split())
visited = [0] * (N + 1)
result = []

find(0, [])

for i in result:
    print(*i)