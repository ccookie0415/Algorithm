H,W = map(int,input().split())

for _ in range(H):
    data = list(input())
    ans = [-1]*W
    tmp = 0

    for i in range(len(data)):
        if data[i] == 'c':
            ans[i] = 0
        elif data[i] == '.':
            if ans[i-1] == -1:
                ans[i] == -1
            else:
                ans[i] = ans[i-1]+1

    print(*ans)
