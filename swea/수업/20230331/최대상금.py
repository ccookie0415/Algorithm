import sys
sys.stdin = open('최대상금.txt','r')

def find(n, num):
    global ans

    if (n,int(''.join(num))) in check:
        return

    check.add((n,int(''.join(num))))

    if n == cnt:
        if ans < int(''.join(num)):
            ans = int(''.join(num))
        return

    for i in range(len(num) - 1):
        for j in range(i+1, len(num)):
            num[i],num[j] = num[j],num[i]
            find(n+1, num)
            num[i],num[j] = num[j],num[i]

T = int(input())

for tc in range(1,T+1):
    lst = list(map(str,input().split()))
    number = list(lst[0])
    cnt = int(lst[1])
    check = set()
    ans = 0

    find(0,number)
    print(f'#{tc} {ans}')