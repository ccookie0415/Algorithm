def binary_search(lst, target, start, end, position):
    global ans

    if start > end:
        return None
    mid = (start + end) // 2

    if lst[mid] == target:
        ans += 1
        return

    elif lst[mid] > target:
        if position == -1:
            return
        return binary_search(lst, target, start, mid-1, -1)

    else:
        if position == 1:
            return
        return binary_search(lst, target, mid+1, end, 1)

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    A_lst = list(map(int,input().split()))
    B_lst = list(map(int,input().split()))
    A_lst.sort()
    ans = 0

    for i in B_lst:
        binary_search(A_lst, i, 0, len(A_lst)-1, 0)

    print(f'#{tc} {ans}')
