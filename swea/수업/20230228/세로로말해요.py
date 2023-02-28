import sys
sys.stdin = open('세로로말해요.txt')

T = int(input())

for tc in range(1,T+1):
    data = [list(map(str,input())) for _ in range(5)]
    print(data)
    arr = list(zip(*data))

    print(arr)


