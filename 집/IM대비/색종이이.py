N = int(input())
arr = [[0] * 1001 for _ in range(1001)]
ans = []

for k in range(1,N+1):
    x,y,width,height = map(int,input().split())
    for i in range(x,x+width):
        for j in range(y,y+height):
            arr[i][j] = k


for k in range(1,N+1):
    cnt = 0
    for i in range(1001):
        for j in range(1001):
            if arr[i][j] == k:
                cnt += 1
    ans.append(cnt)

for i in ans:
    print(i)
