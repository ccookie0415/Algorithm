import sys
sys.stdin = open('testcase/줄세우기.txt','r')

N = int(input())
lst = [0] + list(map(int,input().split()))
ans = [0] * (N+1)
print(lst)

for i in range(0,N+1):
    if lst[i] == 0:
        ans[i] = i
    else:
        ans[i] = i
        for j in range(i-(lst[i]), i+1):
            ans[j] = ans[j-1]

    print(ans)


