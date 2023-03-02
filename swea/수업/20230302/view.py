import sys
sys.stdin = open('view.txt','r')

T = 10

for tc in range(1,T+1):
    tc_num = int(input())
    lst = list(map(int,input().split()))
    cnt = 0

    for i in range(2,len(lst)-2):
        A = lst[i-2:i+3]
        max_ = lst[i]
        max_1 = 0
        for j in range(5):
            if j == 2:
                continue
            else:
                if max_1 < A[j]:
                    max_1 = A[j]
        if max_1 > max_:
            continue
        else:
            cnt += (max_ - max_1)

    print(f'#{tc} {cnt}')
