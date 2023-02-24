import sys
sys.stdin = open('삼성시의 버스 노선.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    for _ in range(N):
        s,e = map(int,input().split())
    
    P = int(input())
    cnt = [0] * P

    for _ in range(N):
        for i in range(s,e):
            cnt[i] += 1

    print(cnt)