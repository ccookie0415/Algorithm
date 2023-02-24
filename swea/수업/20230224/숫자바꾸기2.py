import sys
sys.stdin = open('숫자바꾸기.txt','r')

T = int(input())
for tc in range(1, 1 + T):
    num = list(input())
    A = len(num)
    ans_min = ''.join(num)
    ans_max = ''.join(num)

    for i in range(A - 1):
        for j in range(i + 1, A):
                if i==0 and num[j]=='0':
                    continue
                num[i],num[j]=num[j],num[i]
                if ans_min > ''.join(num):
                    ans_min = ''.join(num)
                if ans_max < ''.join(num):
                    ans_max = ''.join(num)
                num[i],num[j]=num[j],num[i]

    print(f'#{tc} {ans_min} {ans_max}')