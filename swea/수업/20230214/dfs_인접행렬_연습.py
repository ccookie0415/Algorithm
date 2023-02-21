# 인접행렬으로 푸는 방식

import sys
sys.stdin = open('깊이우선탐색.txt', 'r')

adj = [[0]*(V+1) for _ in range(V+1)]
path = []
adj[s][e] = adj[e][s] = 1

def dfs(start):                 # s, e = start 노드, end 노드
    visited = [0] * (V+1)     # V = data 내의 경로를 나타내는 숫자 중 가장 큰 값
    stack = []                  # 모든 경로를 다 거쳤는지 확인하기 위해
    s = start                   # start 값 설정해주어야 함(맨 처음 시작)
    visited[s] = 1              # 시작을 s에서 했으니, 방문했다고 체크해주어야 함
    path.append(s)              # path = 어떤 순서로 이동했는지 확인하기 위해 매번 체크 한다.

    while True:                 # 모든 경로를 다 방문할 때까지
        for e in range(1,V+1):
            if visited[e] == 0 and adj[s][e] == 1:      # 만약, 지금 가려는 e 경로를 거치지 않았고, s와 e가 연결되어있다면
                stack.append(s)                         # 되돌아갈 위치 설정하기
                s = e                                   # s에서 e로 이동했으니, s값을 바꾸어 줌
                path.append(s)                          # path에 이동경로 표시
                visited[s] == 1                         # visited에 방문했다고 체크함.
                break                                   # break하고, 다른 s,e를 기준으로 체크
        else:                                           # 더 이상 연결된 미방문 노드가 없는 경우 (visited[e] == 1 and adj[s][e] == 1:)
            if stack:
                s = stack.pop()
            else :
                break


