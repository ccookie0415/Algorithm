import sys
sys.stdin = open('수영장.txt','r')

def find(n,total):
    global min_

    if min_ <= total:
        return

    if n >= 12:
        min_ = min(min_, total)
        return

    find(n+1, total + cost[0] * month[n])
    find(n+1, total + cost[1])
    find(n+3, total + cost[2])


T = int(input())

for tc in range(1,T+1):
    cost = list(map(int,input().split()))
    month = list(map(int,input().split()))
    min_ = cost[3]

    find(0, 0)
    print(f'#{tc} {min_}')

