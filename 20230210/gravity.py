import sys
sys.stdin = open('input_gravity.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    M = list(map(int,input().split()))
    max_value = 0

    for i in range(len(M)):
        
        print(M[i])


