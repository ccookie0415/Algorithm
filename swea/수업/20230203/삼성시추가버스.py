import sys
sys.stdin = open('input_삼성추가버스.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    dic = {}

    for i in range(1,1001):
        dic[i] = 0

    for i in range(N):
        bus_type, A, B = map(int, input().split())
        for j in range(A,B+1):
            if j == A or j == B:
                dic[j] += 1
            elif bus_type == 1:
                dic[j] += 1
            elif bus_type == 2:
                if A % 2 == 0:
                    if j % 2 == 0:
                        dic[j] += 1
                elif A % 2 == 1:
                    if j % 2 == 1:
                        dic[j] += 1
            elif bus_type == 3:
                if A % 2 == 0:
                    if j % 4 == 0:
                        dic[j] += 1
                if A % 2 == 1:
                    if j % 3 == 0 and j % 10 != 0:
                        dic[j] += 1

    # print(dic)
    print(f'#{tc+1} {max(dic.values())}')


