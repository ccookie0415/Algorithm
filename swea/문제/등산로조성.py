import sys
sys.stdin = open('등산로조성.txt','r')

def dfs()



T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]

    print(arr)