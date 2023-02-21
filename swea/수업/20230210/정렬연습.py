import sys
sys.stdin = open('input_정렬연습.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    num_lst = list(map(int,input().split()))

# 가장 작은 값을 0번
# 그다음 인덱스 1
# 그다음 인덱스 2
#     a = len(num_lst)

    # for i in range(a-1):
    #     minindex = i
    #     for j in range(i+1, a):
    #         if num_lst[j] < num_lst[minindex]:
    #             minindex = j
    #     num_lst[i], num_lst[minindex] = num_lst[minindex], num_lst[i]
    #
    # print(num_lst)

    a = len(num_lst)
    #
    for i in range(a-1):
        minindex = i
        for j in range(i+1, a):
            if num_lst[j] < num_lst[minindex]:
                minindex = j

        num_lst[i],num_lst[minindex] = num_lst[minindex], num_lst[i]

    print(num_lst)

    # for i in range(N-1, 0 ,-1):
    #     for j in range(0,i):
    #         if num_lst[j] > num_lst[j+1]:
    #             num_lst[j],num_lst[j+1] = num_lst[j+1],num_lst[j]
    # print(num_lst)








