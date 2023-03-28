import sys
sys.stdin = open('수영장.txt', 'r')

def find(n, total):
    global ans

    if total > ans:
        return

    if n >= 12:
        if total <= ans:
            ans = total
    else:
        find(n + 1, total + cost[0] * month[n])
        find(n + 1, total + cost[1])
        find(n + 3, total + cost[2])

T = int(input())

for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    month = list(map(int,input().split()))
    ans = cost[3]

    find(0,0)
    print(f'#{tc} {ans}')