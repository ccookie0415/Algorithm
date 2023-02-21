import sys
sys.stdin = open('퀵정렬.txt', 'r')

T = int(input())

def qsort(lst):
    # 종료조건 : 정렬할 요소가 1개라면 종료
    if len(lst) <= 1:
        return lst

    # [1] 단위작업 : p 기준으로 좌/우로 분리
    p = lst.pop()
    left = []
    right = []
    for n in lst:
        if n<p:
            left.append(n)
        else:
            right.append(n)

    # [2] 왼쪽을 정렬한 결과 +[pivot] + 오른쪽을 정렬한 결과
    return qsort(left) + [p] + qsort(right)

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    alst = qsort(lst)
    ans = alst[N//2]

    print(f'#{tc} {ans}')
