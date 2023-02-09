import sys
sys.stdin = open('input_구간합.txt', 'r')

T = int(input())

ans = 0

for tc in range(T):
    N,M = map(int,input().split())
    num_lst = list(map(int,input().split()))
    tmp = 0
    lst = []
print(lst)

    for i in range(0, N-2):
        for j in range(M):
            tmp += num_lst[i+j]
            lst.append(tmp)
        tmp = 0
    print(lst)

