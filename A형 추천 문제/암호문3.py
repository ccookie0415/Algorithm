import sys
sys.stdin = open('암호문3.txt','r')

T = 10

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    M = int(input())
    M_lst = list(map(str,input().split()))



