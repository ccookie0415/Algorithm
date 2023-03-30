import sys
sys.stdin = open('부분집합의합.txt','r')

def find(n,cnt,total):
    global ans

    if cnt > N:
        return

    if total > K:
        return

    if n == len(lst):
        if cnt == N and total == K:
            ans += 1
        return

    find(n+1, cnt+1, total + lst[n])
    find(n+1, cnt, total)

T = int(input())

for tc in range(1,T+1):
    N,K = list(map(int,input().split()))
    lst = [i for i in range(1,13)]
    ans = 0

    find(0,0,0)

    print(f'#{tc} {ans}')
