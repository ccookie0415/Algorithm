L = int(input())
N = int(input())
lst = [0] * (L+1)
ans = [0] * 2
max_pre = 0
max_cur = 0

for k in range(1,N+1):
    start,end = map(int,input().split())

    if end-start > max_pre:
        max_pre = end-start
        ans[0] = k

    for i in range(start,end+1):
        if lst[i] == 0:
            lst[i] = k

for k in range(1,N+1):
    cnt = 0
    for j in range(L):
        if lst[j] == k:
            cnt += 1
    if cnt > max_cur:
        max_cur = cnt
        ans[1] = k

for i in ans:
    print(i)