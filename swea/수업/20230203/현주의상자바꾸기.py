import sys
sys.stdin = open('input_현주의상자바꾸기.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    dic = {}

    for i in range(1, N + 1):
        dic[i] = 0

    for i in range(Q):
        start, end = map(int, input().split())
        for j in range(start, end + 1):
            dic[j] = i + 1

    result = []
    for i in range(1, N + 1):
        result.append(dic[int(i)])

    answer = ' '.join(map(str, result))

    print(f'#{tc} {answer}')
