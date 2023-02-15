# 탐색
# 범위 내 0<= <N, '1'이 아님, 미방문
# while True:
#   for 4/8방향, 연결
#   ni, nj 계산
#   if  범위내, 미방문, '1'이 아니면
#   append(ci,cj) #current i, currentj , 복기 위해서 표시하는 것
#   visited[ni,nj] <= 1, ci,cj = ni,nj
#   else:
#   if stack ==1,  cj,cj <= pop
#   else break

import sys
sys.stdin = open('미로.txt', 'r')

def dfs(si,sj):
    # 필요한 자료형, 플래그, 변수 등 선언
    stack = []

    # 기준점 저장
    ci, cj = si, sj

    # 초기 위치 처리
    visited[ci][cj] = 1

    while True:
        # 4/8/연결된링크... 범위내/미방문/'1'이 아니면 탐색
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj                # 다음좌표 계산
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0 and arr[ni][nj] != '1':
                stack.append((ci,cj))

                ci,cj =ni,nj
                visited[ci][cj] = 1
                break
        else:
            if stack:
                ci, cj = stack.pop()
            else:
                break


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    # 시작/종료 좌표 저장

    for i in range(N):
        for j in range(N):
            if arr[i][j]=='2':
                si,sj = i,j
            elif arr[i][j]=='3':
                ei,ej = i,j

    dfs(si,sj)
    ans = visited[ei][ej]
    print(f'#{tc} {ans}')