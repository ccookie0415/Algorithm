import sys
sys.stdin = open('ladder1.txt','r')

T = 10

for tc in range(1,T+1):
    tc_num = int(input())
    data = [list(map(int,input().split())) for _ in range(100)]

    print(data)