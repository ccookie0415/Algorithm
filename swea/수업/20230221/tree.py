import sys
sys.stdin = open('tree.txt','r')

T = int(input())

for tc in range(1,T+1):
    E,N = map(int,input().split())
    data = list(map(int,input().split()))
    adj = [[] for _ in range(E+2)]

    for i in range(0,E*2-1,2):
        s = data[i]
        e = data[i+1]
        adj[s].append(e)

    while q:

