import sys
sys.stdin = open('testcase/색종이2.txt','r')

N = int(input())
arr = [[0] * 100 for _ in range(100)]
ans = 0
di = [-1,1,0,0]
dj = [0,0,-1,1]

for _ in range(N):
    x,y = map(int,input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if arr[ni][nj] == 1:
                    cnt += 1
            if cnt == 3:
                ans += 1
            elif cnt == 2:
                ans += 2
print(ans)

