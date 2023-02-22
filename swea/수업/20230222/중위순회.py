import sys
sys.stdin = open('중위순회.txt','r')

T = 10

for tc in range(1,T+1):
    N = int(input())

    for _ in range(N):
        arr = list(input().split())

        print(arr)



