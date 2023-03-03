import sys
sys.stdin = open('이진탐색.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = [0] * (N+1)

    for i in range(N):

