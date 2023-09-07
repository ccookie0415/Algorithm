T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst_ = [0] * N

    for _ in range(M):
        L,R = map(int,input().split())

        for i in range(L-1, R):
            lst_[i] = L

    print(lst_)