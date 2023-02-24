import sys
sys.stdin = open('testcase/방배정.txt','r')

N,K = map(int,input().split())
ans = 0

dic_0 = {}
dic_1 = {}

for i in range(1,7):
    dic_0[i] = 0
    dic_1[i] = 0

for _ in range(N):
    S,Y = map(int,input().split())

    if S == 0:
        dic_0[Y] += 1
    else:
        dic_1[Y] += 1

for value in dic_0.values():
    if value != 0:
        while True:
            if value <= K:
                ans += 1
                break
            else:
                value = value - K
                ans += 1

for value in dic_1.values():
    if value != 0:
        while True:
            if value <= K:
                ans += 1
                break
            else:
                value = value - K
                ans += 1

print(ans)




