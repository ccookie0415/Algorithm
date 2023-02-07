import sys
sys.stdin = open('input_이진탐색2.txt', 'r')

T = int(input())

def binary_search(start, end, D):
    cnt = 0

    while start <= end:
        mid = int((start + end)/2)

        if mid == D:
            return cnt

        elif mid > D:
            end = mid
            cnt += 1

        else:
            start = mid
            cnt += 1

    return None

# P = 책의 전체 쪽 수 Pa = A가 찾을 쪽 번호, Pb = B가 찾을 쪽 번호
for tc in range(1, T+1):
    P,Pa,Pb = map(int,input().split())
    start = 1
    end = P
    ans = 0

    if binary_search(start, end, Pa) < (binary_search(start, end, Pb)):
        ans = 'A'
    elif binary_search(start, end, Pa) > (binary_search(start, end, Pb)):
        ans = 'B'
    else:
        ans = 0

    print(f'#{tc} {ans}')
