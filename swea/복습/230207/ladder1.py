import sys
sys.stdin = open('ladder1.txt','r')

di = [0,0,-1,1]
dj = [-1,1,0,0]

T = 3

for tc in range(1,T+1):
    tc_num = int(input())
    arr = [list(map(int,input().split())) for _ in range(100)]
    ans = 0

    for j in range(100):
        if arr[0][j] == 1:
            start_i = 0
            start_j = j

        print(start_i, start_j)

