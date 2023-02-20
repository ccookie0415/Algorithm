import sys
sys.stdin = open('algo2_sample_in.txt','r')

di = [0,1,0,-1]                             # 본 예시에서, 0 은 오른쪽방향, 1은 아래방향, 2는 왼쪽방향, 3은 위쪽방향을 나타내므로 좌표 설정한다.
dj = [1,0,-1,0]

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]    # 지도 입력 받음.
    visited = [([0] * N) for _ in range(N)]                     # 로봇이 갔던 곳을 체크하기 위해 지도와 똑같은 visited 배열 생성해줌.
    path = []                                                   # 이동 경로를 표시하기 위해 path 라는 리스트 만들어 줌

    i = 0                          # 로봇이 N*N 구역 왼쪽 맨 윗칸에서 움직인다고 했으므로
    j = 0                          # i = 0, j = 0으로 초기값 설정해줌.
    a = 0                          # a는 로봇의 방향을 설정해주기 위해 만들어 줌.
    path.append(arr[i][j])         # 초기 0,0 시작점을 이동경로 리스트에 넣어줌
    visited[i][j] = 1              # 0,0을 방문함을 체크해주어야 하니까
    for k in range(N*N):           # 지도의 크기보다는 더 이동하지 않을거니까 N*N만큼 반복

        if arr[i][j] == 0:         # 0 오른쪽방향
            a = 0
        if arr[i][j] == 1:         # 1 아래방향
            a = 1
        if arr[i][j] == 2:         # 2 왼쪽방향
            a = 2
        if arr[i][j] == 3:         # 3 위쪽방향
            a = 3
        ni = i + di[a]             # 다음에 갈 곳의 좌표를 임시로 찾아봄
        nj = j + dj[a]

        if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:    # 만약에 다음에 갈 곳이 범위 안에 있고, 방문하지 않았다면
            ni = i + di[a]        # ni, nj를 선언해서
            nj = j + dj[a]
            i = ni                # i와 j에 넣어준다.
            j = nj
            visited[ni][nj] = 1   # ni, nj 다음에 방문할 거니까
            path.append(arr[ni][nj])    # 이동경로에 넣어줌
        else:                     # 그 외의 경우라면
            break                 # 갈 곳이 없다는 것이니까 break

    stack = []                    # 중복 제거를 위해 stack 만들어 줌

    for token in path:
        if not stack:                   # stack 이 비었다면 이동경로에 있는 token push
            stack.append(token)
        elif stack:                     # stack이 있다면 token을 stack의 가장 위와 비교해서
            if token != stack[-1]:      # 같지 않다면 stack에 token push
                stack.append(token)

    ans = []                            # 답을 출력 예시와 같이 출력하기 위함
    for i in stack:
        ans.append(str(i))


    ans = ' '.join(ans)
    print(f'#{tc}', *stack)