import sys
sys.stdin = open('testcase/딱지놀이.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())

    for _ in range(N):
        A = list(map(int,input().split()))
        B = list(map(int,input().split()))
        a_lst = [0] * 5
        b_lst = [0] * 5

        for i in A[1:]:
            a_lst[i] += 1

        for j in B[1:]:
            b_lst[j] += 1

        for i in range(4,0,-1):
            if a_lst[i] > b_lst[i]:
                ans = 'A'
                break
            elif a_lst[i] < b_lst[i]:
                ans = 'B'
                break
            else:
                ans = 'D'

        print(ans)
