import sys
sys.stdin = open('ATM.txt','r')

N = int(input())
lst = list(map(int,input().split()))


for i in range(N-1,0,-1):
    for j in range(i):
        if lst[j] > lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

total = lst[0]

for i in range(1,N):
    lst[i] = lst[i-1]+lst[i]
    total += lst[i]

print(total)




