import sys
sys.stdin = open('연산.txt','r')

from collections import deque

def bfs():

    q = deque([(N, 0)])
    dic = dict()

    while q:
        now, count = q.popleft()

        if dic.get(now, 0):
            continue
        dic[now] = 1

        if now == M:
            return count
        count += 1

        if 0 < now - 1 <= 10**6:
            q.append((now-1, count))

        if 0 < now + 1 <= 10**6:
            q.append((now+1, count))

        if 0 < now * 2 <= 10**6:
            q.append((now*2, count))

        if 0 < now - 10 <= 10**6:
            q.append((now-10, count))

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    ans = bfs()
    print(f'#{tc} {ans}')