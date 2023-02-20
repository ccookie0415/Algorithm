import sys
sys.stdin = open('자기방으로돌아가기.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    visited = [0] * 201

    for _ in range(N):
        s,e = map(int,input().split())

        if s>e:
            s,e = e,s

        for i in range((s-1)//2,(e-1)//2 + 1):
            visited[i] += 1

    print(f'#{tc} {max(visited)}')