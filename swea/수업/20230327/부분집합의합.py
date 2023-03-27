T = int(input())
A = [1,2,3,4,5,6,7,8,9,10,11,12]
len_A = len(A)

for t in range(1, T+1):
    N, K = map(int, input().split())
    subset = []

    for i in range(1<<len_A):
        temp = []
        for j in range(len_A):
            if i & (1<<j):
                temp.append(A[j])
        subset.append(temp)

    cnt = 0

    for set in subset:
        total = 0
        if len(set) == N:
            for num in set:
                total += num
            if total == K:
                cnt += 1

    print(f'#{t} {cnt}')
