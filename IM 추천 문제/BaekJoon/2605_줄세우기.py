import sys
sys.stdin = open('testcase/줄세우기.txt','r')

N = int(input())
lst = [0] + list(map(int,input().split()))
ans = [0] * (N+1)

for i in range(0,N+1):
    ans[i] = i
    if lst[i] != 0:
        for j in range(i,i-lst[i],-1):
            ans[j],ans[j-1] = ans[j-1],ans[j]


print(*ans[1:])


