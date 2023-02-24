import sys
sys.stdin = open('특별한정렬.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    ans = []

    for i in range(N-1,0,-1):
        for j in range(i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

    a = 1
    b = 0

    for i in range(10):
        if i % 2 == 0:
            ans.append(lst[-a])
            a += 1
        else:
            ans.append(lst[b])
            b += 1

    print(f'#{tc}',*ans)