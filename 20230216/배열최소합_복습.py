import sys
sys.stdin = open('부분집합의합2.txt', 'r')

T = int(input())

# A = [1,2,3,4,5,6,7,8,9,10,11,12]
# N = A의 부분집합 원소의 개수
# K = N개의 원소를 가진 부분집합의 원소의 합

for tc in range(1,T+1):
    set_,K = map(int,input().split())
    N = len(set_)


