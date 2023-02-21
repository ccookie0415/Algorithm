import sys
sys.stdin = open('input_정렬연습.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num_lst = list(map(int,input().split()))
#
    for i in range(N-1,0,-1):
        for j in range(0,i):
            if num_lst[j] > num_lst[j+1]:
                num_lst[j],num_lst[j+1] = num_lst[j+1],num_lst[j]

    print(num_lst)

