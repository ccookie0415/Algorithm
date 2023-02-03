import sys
sys.stdin = open('input_기차사이의파리.txt', 'r')

T = int(input())

for tc in range(T):
    D,B,A,F = map(int,input().split())

    print(f'#{tc+1} {(D / (A + B)) * F}')