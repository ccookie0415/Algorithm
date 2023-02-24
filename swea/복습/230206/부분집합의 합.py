import sys
sys.stdin = open('부분집합의 합.txt','r')

T = int(input())

for tc in range(1,T+1):
    lst = list(map(int,input().split()))

    for i in range(10):
        