import sys
sys.stdin = open('전기버스2.txt','r')

def find(current, cnt, fuel):
    global ans

    if cnt >= ans:
        return

    if current == N:
        if ans > cnt:
            ans = cnt
        return

    find(current + 1, cnt + 1, battery[current] - 1)

    if fuel > 0:
        find(current + 1, cnt, fuel - 1)

T = int(input())

for tc in range(1,T+1):
    lst = list(map(int,input().split()))
    N = lst[0]
    battery = [0] + lst[1:]
    ans = 99999999

    find(1,0,battery[1])
    print(f'#{tc} {ans}')
