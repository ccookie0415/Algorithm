import sys
sys.stdin = open('input_gravity.txt', 'r')

# T = int(input())
#
# for tc in range(T):
#     N = int(input())
#     box = list(map(int,input().split()))
#
#     for i in range(N-1, 0, -1):
#         for j in range(0,i):
#             if box[j] < box[j+1]:
#                 box[j], box[j+1] = box[j+1], box[j]
#
#         answer = N - box[0]
#
#     print(answer)