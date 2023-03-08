import sys
sys.stdin = open('14501_퇴사.txt','r')

N = int(input())
data= []
ans = [0]*(N+1)

for _ in range(N):
    a,b= map(int,input().split())
    data.append((a,b))

print(data)

for i in range(N-1,-1,-1):
    if i + data[i][0] > N:
        ans[i] = ans[i+1]
    else:
        ans[i] = ans

print(ans)
