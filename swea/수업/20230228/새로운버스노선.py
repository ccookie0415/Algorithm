import sys
sys.stdin = open('새로운버스노선.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    dic = {}

    for i in range(1, 1001):
        dic[i] = 0

    ans = 0

    for _ in range(N):
        bus_type,A,B = map(int,input().split())

        for i in range(A,B):
            if bus_type == 1:
                dic[i] += 1

            if bus_type == 2:
                if A % 2 == 0 and i % 2 == 0:
                    dic[i] += 1
                elif A % 2 == 1 and i % 2 == 1:
                    dic[i] += 1

            if bus_type == 3:
                if A % 2 == 0 and i % 4 == 0:
                    dic[i] += 1
                elif A % 2 == 1 and i % 3 == 0 and i % 10 != 0:
                    dic[i] += 1

    for value in dic.values():
        if value > ans:
            ans = value

    print(f'#{tc} {ans}')
