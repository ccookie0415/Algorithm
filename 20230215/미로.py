import sys
sys.stdin = open('미로.txt' , 'r')

T = int(input())
di = [-1,1,0,0]
dy = [0,0,-1,1]

for tc in range(1,T+1):
    N = int(input())
    arr = [['1'] * (N+2)] + [['1']+list(input())+['1'] for _ in range(N)] + [['1'] * (N+2)]
    visited = [[0]*N for _ in range(N)]


    for i in range(N+2):
        for j in range(N+2):
            if arr[i][j] == '2':
                y,x = i,j




    ans = visited[ei][ej]
    print(f'#{tc} {ans}')