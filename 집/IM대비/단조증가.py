import sys
sys.stdin = open('단조증가.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    data = list(map(int,input().split()))
    max_ = 0
    ans = 0

    for i in range(N):
        for j in range(i+1,N):
            num_lst = []
            num = data[i]*data[j]
            num = str(num)
            for k in range(len(num)):
                num_lst.append(num[k])
                cnt = 0
                if len(num_lst) == 1:
                    continue
                else:
                    for l in range(1,len(num_lst)):
                        if num_lst[l-1] < num_lst[l]:
                            cnt += 1
                    if max_ <= cnt:
                        if max_ < cnt:
                            max_ = cnt
                            ans = int(num)
                        elif max_ == cnt:
                            if ans < num:
                                ans = int(num)

    if max_ == 0:
        print(f'#{tc}',-1)
    else:
        print(f'#{tc} {ans}')