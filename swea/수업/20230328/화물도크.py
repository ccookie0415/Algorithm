import sys
sys.stdin = open('화물도크.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = []
    stack = []
    n = 0
    cnt = 1

    for _ in range(N):
        s,e = map(int,input().split())
        lst.append((e,s))

    A = len(lst)
    lst.sort()
    stack.append(lst[0])

    while True:
        a,b = stack.pop()
        if n == A:
            break
        else:
            if lst[n][1] >= a:
                cnt += 1
                stack.append(lst[n])
                n += 1
            else:
                stack.append((a,b))
                n += 1


    print(f'#{tc} {cnt}')







