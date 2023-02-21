import sys
sys.stdin = open('암호생성기.txt' ,'r')

T = 10

for tc in range(1,T+1):
    tc_num = int(input())
    q = list(map(int,input().split()))
    break_ = 0

    while True:
        if break_ == 1:
            break
        for i in range(1,6):
            t = q.pop(0)
            if t <= i:
                q.append(0)
                break_ = 1
                break
            q.append(t - i)
    print(f'#{tc}',*q)
