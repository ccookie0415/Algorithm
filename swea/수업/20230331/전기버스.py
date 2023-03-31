import sys
sys.stdin = open('전기버스2.txt','r')

def find(n, cnt, fuel):
    global ans

    if cnt >= ans:
        return

    if n == N-1:
        if cnt < ans:
            ans = cnt
        return

    find(n+1, cnt+1, battery[n] - 1)

    if fuel > 0:
        find(n+1, cnt, fuel-1)

T = int(input())

for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    N = lst[0]
    battery = lst[1:]
    ans = 999999999

    find(0,0,battery[0])
    print(f'#{tc} {ans}')