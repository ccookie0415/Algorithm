import sys
sys.stdin = open('이진힙.txt','r')

def enqueue(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c // 2
    while p > 0 and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    lst = list(map(int,input().split()))
    last = 0
    heap = [0] * (N+1)
    total = 0


    for i in range(N):
        enqueue(lst[i])

    while last != 0:
        last = last // 2
        total += heap[last]

    print(f'#{tc} {total}')