import sys
sys.stdin = open('숫자바꾸기.txt','r')

T = int(input())

for tc in range(1,T+1):
    num = list(map(int,input()))
    num2 = num.copy()
    A = len(num)
    min_ = num[0]
    min_idx = 0
    max_ = num[0]
    ans_min = int(''.join(map(str,num)))
    ans_max = int(''.join(map(str,num)))

    for i in range(A):
        if num[i] != 0:
            if num[i] < min_:
                min_ = num[i]
                min_idx = i
            elif num[i] > max_:
                max_ = num[i]
                max_idx = i

    for i in range(A):
        if num[i] != 0:
            if min_2 > num[i] > min_:
                min_2 = num[i]
                min_idx2 = i
            elif max_2 < num[i] < max_:
                max_2 = num[i]
                max_idx2 = i

    if min_idx != 0 and max_idx != 0:
        num[min_idx],num[max_idx] = num[max_idx],num[min_idx]
        ans_1 = int(''.join(map(str, num)))
        if ans_1 > ans_max:
            ans_max = ans_1
        elif ans_1 < ans_min:
            ans_min = ans_1

    elif min_idx == 0:
        num[min_idx2], num[max_idx] = num[max_idx], num[min_idx2]
    elif max_idx == 0:
        num[min_idx], num[max_idx2] = num[max_idx2], num[min_idx]

    print(ans_min, ans_max)
    ans_1 = int(''.join(map(str,num)))

    print(f'#{tc} {ans_min} {ans_max}')
