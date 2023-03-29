import sys
sys.stdin = open('요리사.txt','r')

def find(n,a_lst,b_lst):
    global ans

    if n == N:
        if len(a_lst) == A and len(b_lst) == A:
            value_a = value_b = 0
            for i in range(A):
                for j in range(A):
                    value_a += arr[a_lst[i]][a_lst[j]]
                    value_b += arr[b_lst[i]][b_lst[j]]

            if abs(value_a - value_b) < ans:
                ans = abs(value_a - value_b)

        return

    find(n+1, a_lst + [n], b_lst)
    find(n+1, a_lst, b_lst + [n])


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    A = N//2
    ans = 999999999999
    arr = [list(map(int,input().split())) for _ in range(N)]

    a_lst = []
    b_lst = []

    find(0,a_lst,b_lst)
    print(f'#{tc} {ans}')

