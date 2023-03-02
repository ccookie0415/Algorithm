import sys
sys.stdin = open('파스칼의삼각형.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = []

    for k in range(1,N):
        arr.append([1]*k)

