import sys
sys.stdin = open('배열최소합.txt','r')

def find(row):
    global sum, ans

    if ans < sum:
        return

    if row == N:
        if sum < ans:
            ans = sum
        return

    for col in range(N):
        if not visited[col]:
            visited[col] = 1
            sum += arr[row][col]
            find(row + 1)
            visited[col] = 0
            sum -= arr[row][col]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    visited = [0] * N
    sum = 0
    ans = 999999

    find(0)

    print(f'#{tc} {ans}')