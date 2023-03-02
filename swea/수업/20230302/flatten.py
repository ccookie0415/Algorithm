import sys
sys.stdin = open('flatten.txt','r')

def max_(lst):
    max_ = 0
    max_idx = 0
    for i in range(len(lst)):
        if lst[i] > max_:
            max_ = lst[i]
            max_idx = i
    return max_, max_idx

def min_(lst):
    min_ = 101
    min_idx = 0
    for i in range(len(lst)):
        if lst[i] < min_:
            min_ = lst[i]
            min_idx = i
    return min_, min_idx

T = 10

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))

    while N:
        max_idx = max_(lst)[1]
        min_idx = min_(lst)[1]
        lst[max_idx] -= 1
        lst[min_idx] += 1

        N -= 1
        answer = max_(lst)[0] - min_(lst)[0]

    print(f'#{tc} {answer}')




    # print(lst)

