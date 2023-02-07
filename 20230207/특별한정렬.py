import sys
sys.stdin = open('input_특별한정렬.txt', 'r')

#가장 큰 수, 가장 작은 수, 2번째 큰 수, 2번째 작은 수

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    a_lst = list(map(int,input().split()))

    for i in range(1, N+1):
        for i in range(N-1, 0, -1):
            for j in range(0,i):
                if a_lst[j] > a_lst[j+1]:
                    a_lst[j], a_lst[j+1] = a_lst[j+1], a_lst[j]

    new_lst = [0] * N
    num_1 = -1
    num_2 = 0
    for n_1 in range(0, N, 2):
        new_lst[n_1] = a_lst[num_1]
        num_1 -= 1

    for n_2 in range(1, N+1 ,2):
        new_lst[n_2] = a_lst[num_2]
        num_2 += 1

    ans = ' '.join(map(str,(new_lst[:10])))

    print(f'#{tc} {ans}')



