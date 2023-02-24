import sys
sys.stdin = open('이진탐색.txt','r')

T = int(input())

for tc in range(1,T+1):
    P,A,B = map(int,input().split())
    l = 1
    r = P
    c = int((l+r)/2)
    print(l,r,c)