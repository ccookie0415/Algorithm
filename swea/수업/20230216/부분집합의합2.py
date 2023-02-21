import sys
sys.stdin = open('부분집합의합2.txt', 'r')

# N : 부분집합 원소의 수
# K : 부분 집합의 합

T = int(input())

for tc in range(1,T+1):
    N,K = map(int,input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    subset = [[]]
    arr = []
    cnt = 0

    for i in A:
        L = len(subset)
        for l in range(L):
            subset.append(subset[l] + [i])

    for i in subset:
        if len(i) == N:
            arr.append(i)

    for i in arr:
        sum = 0
        for j in range(0,N):
            sum += i[j]
        if sum == K:
            cnt += 1


    print(f'#{tc} {cnt}')