import sys
sys.stdin = open('노드합.txt', 'r')

T =int(input())

for tc in range(1,T+1):
    N,M,L = map(int,input().split())                # N : 노드의 개수, M : 리프 노드의 개수, L : 값을 출력할 노드 번호
    tree = [0] * (N+1)
    root = 1

    for _ in range(M):
        node, num = map(int,input().split())
        tree[node] = num


    for i in range(N-M,0,-1):
        if 2*i + 1 > N:
            tree[i] = tree[2*i]
        else:
            tree[i] = tree[2*i] + tree[2*i+1]

    print(f'#{tc} {tree[L]}')




