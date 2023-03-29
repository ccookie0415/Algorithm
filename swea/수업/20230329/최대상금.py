import sys
sys.stdin = open('최대상금.txt','r')
sys.setrecursionlimit(10**6)

def find(n, num):
    global ans

    if (n,int(''.join(num))) in check:
        return

    check.add((n,int(''.join(num))))

    if n == N:
        if int(''.join(num)) > ans:
            ans = int(''.join(num))
        return

    for i in range(len(num)-1):
        for j in range(i+1,len(num)):
            num[i],num[j] = num[j],num[i]
            find(n+1,num)
            num[i],num[j] = num[j],num[i]

T = int(input())

for tc in range(1,T+1):
    lst = list(map(str,input().split()))
    num = list(lst[0])
    ans = 0
    N = int(lst[1])
    check = set()

    find(0,num)

    print(f'#{tc} {ans}')
