# import sys
# sys.stdin = open('testcase/cake.txt','r')

T = int(input())

for tc in range(1,T+1):
    L = int(input())
    N = int(input())
    ans = [0] * 2
    cake = [0]*(L+1)
    max_ = 0
    cake_max = 0

    for k in range(1,N+1):
        start,end = map(int,input().split())
        if end-start > max_:
            max_ = end-start
            ans[0] = k

        for i in range(start,end+1):
            if cake[i] == 0:
                cake[i] = k

    for k in range(1,N+1):
        cnt = 0
        for j in cake:
            if j == k:
                cnt += 1
        if cnt > cake_max:
            cake_max = cnt
            ans[1] = k

    for i in ans:
        print(i)

