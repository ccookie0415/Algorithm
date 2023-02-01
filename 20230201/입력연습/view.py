import sys
sys.stdin = open('input_view.txt', 'r')

T = int(input())

for _ in range(0,T):
    num_lst = list(map(int,input().split()))

    print(num_lst)