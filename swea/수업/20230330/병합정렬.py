import sys
sys.stdin = open('병합정렬.txt', 'r')

def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    left_ = merge_sort(left)
    right_ = merge_sort(right)
    return merge(left_, right_)

def merge(left_,right_):
    global cnt
    i,j = 0,0
    lst = []

    if left_[-1] > right_[-1]:
        cnt += 1

    while i < len(left_) and j < len(right_):
        if left_[i] < right_[j]:
            lst.append(left_[i])
            i += 1
        else:
            lst.append(right_[j])
            j += 1

    while i < len(left_):
        lst.append(left_[i])
        i += 1

    while j < len(right_):
        lst.append(right_[j])
        j += 1

    return lst

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    cnt = 0

    ans = (merge_sort(lst))[N//2]

    print(f'#{tc} {ans} {cnt}')
