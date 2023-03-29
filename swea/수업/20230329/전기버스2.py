import sys
sys.stdin = open('전기버스2.txt','r')

def find(current, cnt):
    global ans

    if cnt >= ans:
        return

    if current >= N:
        if cnt < ans:
            ans = cnt
        return

    for i in range(lst[current]):
        find(current+i+1, cnt+1)


T = int(input())

for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    N = lst[0]
    battery = [0] + lst[1:]
    ans = N+1

    find(1,0)
    print(f'#{tc} {ans-1}')