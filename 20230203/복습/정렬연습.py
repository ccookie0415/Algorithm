import sys
sys.stdin = open('input_정렬연습.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    num = list(map(int,input().split()))

    for i in range(N-1, 0, -1):
        for j in range(0, i):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    # print(num)
    num_arr = (' '.join(map(str,num)))
    print(num_arr)