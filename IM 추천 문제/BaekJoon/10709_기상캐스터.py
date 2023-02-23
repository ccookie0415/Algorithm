import sys
sys.stdin = open('기상캐스터.txt','r')

T = int(input())

for tc in range(1,T+1):
    H,W = map(int,input().split())
    arr = [list(map(str,input())) for _ in range(H)]
    ans = [[-1]*W for _ in range(H)]

    c = 0
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'c':
                ans[i][j] = c

    for i in range(H):
        for j in range(W):
            if ans[i][j] == 0:
                cnt = 1
                for k in range(j+1,W):
                    if ans[i][k] != 0:
                        ans[i][k] = cnt
                        cnt += 1
    for i in range(H):
        print(*ans[i])



H,W = map(int,input().split())
arr = [list(map(str,input())) for _ in range(H)]
ans = [[-1]*W for _ in range(H)]

c = 0
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'c':
            ans[i][j] = c

for i in range(H):
    for j in range(W):
        if ans[i][j] == 0:
            cnt = 1
            for k in range(j+1,W):
                if ans[i][k] != 0:
                    ans[i][k] = cnt
                    cnt += 1
for i in range(H):
    print(*ans[i])





