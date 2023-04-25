def check(arr, x, y):

    di = [1,-1,0,0]
    dj = [0,0,1,-1]

    for k in range(4):
        ni = x + di[k]
        nj = y + dj[k]

        if ni < 0 or ni >= N or nj < 0 or nj >= M:
            continue

        if arr[ni][nj] == 1:
            continue

        if arr[ni][nj] != 2:
            arr[ni][nj] = 2
            check(arr, ni, nj)


def dfs(count, arr):
    global answer

    if count == 3:
        temp_graph = [i[:] for i in arr]

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    check(temp_graph, i, j)
        safe_count = 0

        for i in range(N):
            for j in range(M):
                if temp_graph[i][j] == 0:
                    safe_count += 1
        if answer < safe_count:
            answer = safe_count

    else:
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    count += 1
                    arr[i][j] = 1
                    dfs(count, arr)
                    arr[i][j] = 0
                    count -= 1


N, M = list(map(int, input().split()))
arr = [list(map(int,input().split())) for _ in range(N)]
answer = 0
dfs(0, arr)

print(answer)