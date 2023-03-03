import sys
sys.stdin = open('자기방으로돌아가기.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    visited = [0]*201
    max_ = 0

    for _ in range(N):
        start,end = map(int,input().split())

        if start>end:
            start,end = end,start

        for i in range((start-1)//2,(end-1)//2+1):
            visited[i] += 1

    for i in visited:
        if i > max_:
            max_ = i

    print(f'#{tc} {max_}')