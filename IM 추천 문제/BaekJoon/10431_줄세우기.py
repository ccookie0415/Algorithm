import sys
sys.stdin = open('testcase/10431_줄세우기.txt','r')

T = int(input())

for tc in range(1,T+1):
    data = list(map(int,input().split()))
    N = 20
    tc_num = data[0]
    data = data[1:]
    cnt = 0

    for i in range(N-1,0,-1):
        for j in range(i):
            if data[j] > data[j+1]:
                cnt += 1
                data[j],data[j+1] = data[j+1],data[j]

    print(f'{tc} {cnt}')