N = int(input())
arr = [[0] * 100 for _ in range(100)]
di = [1,0,-1,0]
dj = [0,1,0,-1]
ans = 0

for _ in range(N):
    x,y = map(int,input().split())

    for i in range(y,y+10):
        for j in range(x,x+10):
            arr[i][j] = 1

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            cnt = 0
            for k in range(4):
                ni = i + di[k]
                nj = j + dj[k]
                if 0 <= ni < 100 and 0 <= nj < 100 and arr[ni][nj] == 1:
                    cnt += 1
            if cnt == 2:
                ans += 2
            elif cnt == 3:
                ans += 1

print(ans)