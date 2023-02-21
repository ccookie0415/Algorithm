import sys
sys.stdin = open('input_삼성시버스.txt', 'r')

T = int(input())

for tc in range(T):
    N = int(input())
    bus_dic = {}

    for i in range(1,5001):
        bus_dic[i] = 0

    for i in range(N):
        start,end = map(int,input().split())
        for j in range(start,end+1):
            bus_dic[j] += 1

    P = int(input())
    result = []

    for i in range(P):
        result.append(bus_dic[int(input())])

    answer = ' '.join(map(str,result))

    print(f'#{tc+1} {answer}')


