import sys
sys.stdin = open('input_델타검색.txt', 'r')

T=int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    # [1] 전체 루프를 순회하면서, 각 요소 4방향 절대값 합을 누적
    for i in range(N):
        for j in range(N):
            # 4방향에 대한 처리 진행
            for di,dj in ((-1,0),(-1,0),(0,-1),(0,1)):
                ni,nj = i+di, j+dj #이동할(next) i, j
                # 범위내인지 확인 후 사용
                if 0 <=ni<N and 0<=nj<N:
                    if arr[i][j]>arr[ni][nj]:
                        ans += (arr[i][j] - arr[ni][nj])
                    else:
                        ans += (arr[ni][nj] - arr[i][j])

    print(f'#{tc+1} {ans}')