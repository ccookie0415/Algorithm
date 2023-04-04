def find_set(x):
    while x != par[x]:
        x = par[x]
    return x


def union_set(x, y):
    par[find_set(y)] = find_set(x)
    return x


T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    lst = list(map(int,input().split()))
    par = [i for i in range(N+1)]


    for i in range(M):
        union_set(lst[2*i], lst[2*i+1])

    result = set()

    for j in range(len(par)):
        if j != 0:
            result.add(find_set(j))

    print(f'#{tc} {len(result)}')

