def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[0]
    other = lst[1:]

    left_side = [i for i in other if i <= pivot]
    right_side = [i for i in other if i > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    ans = quick_sort(lst)[N//2]

    print(f'#{tc} {ans}')
