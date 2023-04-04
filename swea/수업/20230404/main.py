def find(n, current, total):
    global ans

    if total > ans:
        return

    if n == N-1:                                    # 다 방문했다면    # 조건을 만족하려면 a가 먼저 check_2에 넘어가고, b가 check에 남아있어야하니까
        if total + arr[current][0] < ans:       # 이 때 비교해주면 됨
            ans = total + arr[current][0]
        return

    for j in range(1,N):                            # 사무실 들르기
        if visited[j] == 0:                         # 방문안했다면
            visited[j] = 1                          # 방문체크
            find(n+1, j, total + arr[current][j])      # 변수 재설정 후 find함수 부름
            visited[j] = 0                                          # 다시 방문 안했음 체크

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    ans = 9999999999999
    visited = [0] * N                               # visited배열

    find(0,0,0)                                  # 함수 호출

    print(f'#{tc} {ans}')