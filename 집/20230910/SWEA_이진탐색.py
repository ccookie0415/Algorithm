def binary_search(start, end):
    while start <= end:

        mid = (start + end) // 2

        if lst[mid] == D:
            return mid

        elif lst[mid] > D:
            end = mid - 1

        else:
            start = mid + 1

    return None

T = int(input())

for tc in range(1,T+1):
    N,D = map(int,input().split())
    lst = list(map(int,input().split()))

    result = binary_search(0,N-1)

    if result == None:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result + 1}')