import sys
sys.stdin = open('이진탐색.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ans1 = N//2 + 1
    ans2 = ans1
    print(f'#{tc}')