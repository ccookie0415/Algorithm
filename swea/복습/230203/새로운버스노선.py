import sys
sys.stdin = open('새로운버스노선.txt','r')

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    bus_dic = {}

    for i in range(1001):
        bus_dic[i] = 0

    for _ in range(N):
        bus_type, A, B = map(int,input().split())
        for i in range(A,B):
            if bus_type == 1:
                bus_dic[i] += 1
            elif bus_type == 2:
                if A % 2 == 0:
                    if i % 2 == 0:
                        bus_dic[i] += 1
                else:
                    if i % 2 == 1:
                        bus_dic[i] += 1

            elif bus_type == 3:
                if A % 2 == 0:
                    if i % 4 == 0:
                        bus_dic[i] += 1
                else:
                    if i % 3 == 0 and i % 10 != 0:
                        bus_dic[i] += 1
    max_ = 0
    for values in bus_dic.values():
        if values > max_:
            max_ = values

    print(f'#{tc} {max_}')
