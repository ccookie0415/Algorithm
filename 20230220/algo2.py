import sys
sys.stdin = open('algo2_sample_in.txt', 'r')

di = [0,1,0,-1]
dj = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    visited = [([0] * N) for _ in range(N)]
    path = []

    i = 0
    j = 0
    a = 0
    path.append(arr[i][j])
    for k in range(N*N):

        if arr[i][j] == 0:
            a = 0
        if arr[i][j] == 1:
            a = 1
        if arr[i][j] == 2:
            a = 2
        if arr[i][j] == 3:
            a = 3
        ni = i + di[a]
        nj = j + dj[a]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
            ni = i + di[a]
            nj = j + dj[a]
            i = ni
            j = nj
            visited[ni][nj] = 1
            path.append(arr[ni][nj])
        else:
            break

    stack = []

    for token in path:
        if not stack:
            stack.append(token)
        elif stack:
            if token != stack[-1]:
                stack.append(token)

    ans = []
    for i in stack:
        ans.append(str(i))

    ans = ' '.join(ans)

    print(f'#{tc} {ans}')




