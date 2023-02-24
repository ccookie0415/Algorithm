import sys
sys.stdin = open('현주의상자바꾸기.txt','r')

T = int(input())

for tc in range(1,T+1):
    N,Q = map(int,input().split())
    lst = [0] * N

    for _ in range(Q):
        L,R = map(int,input().split())

        for i in range(L-1,R):
            lst[i] = L

    print(f'#{tc}', *lst)
