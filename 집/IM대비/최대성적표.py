import sys
sys.stdin = open('최대성적표.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    data = list(map(int,input().split()))
    data.sort()
    ans = data[-K:]
    total = 0

    for i in ans:
        total += i

    print(f'#{tc} {total}')