def find(n, A_lst, B_lst):
    global ans

    if n == N:
        if len(A_lst) == A and len(B_lst) == A:
            value_a = 0
            value_b = 0
            for i in range(A):
                for j in range(A):
                    value_a += arr[A_lst[i]][A_lst[j]]
                    value_b += arr[B_lst[i]][B_lst[j]]
            if abs(value_a - value_b) < ans:
                ans = abs(value_a - value_b)
        return

    find(n+1, A_lst + [n], B_lst)
    find(n+1, A_lst, B_lst + [n])

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    A = N//2
    ans = 9999999

    A_lst = []
    B_lst = []

    find(0,A_lst,B_lst)

    print(f'#{tc} {ans}')