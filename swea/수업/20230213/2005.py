import sys
sys.stdin = open('2005.txt', 'r')

# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     stack = []
#
#
#     print(f'#{tc}')
#     for i in range(N):
#         tmp = []
#         for j in range(i+1):
#             if j == 0 or j == i:
#                 tmp.append(1)
#             else:
#                 tmp.append(stack[i-1][j] + stack[i-1][j-1])
#         stack.append(tmp)
#
#         print(*stack[i])

# 다른 방법
# [1] 문제 설명대로 구현
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [[0] * (N+1) for _ in range(N+1)]
#     arr[1][1] = 1           #[1] 첫 줄은 항상 1
#     for i in range(2,N+1):
#         for j in range(1, i+1):
#             # 한 행 위의 왼쪽과 한 줄 위 값의 합
#             arr[i][j] = arr[i-1][j-1]+arr[i-1][j]
#
#     # 모두 출력이 아닌, 0이 아닌 값만 출력(또는 범위)
#
#     print(f'#{tc}')
#     for i in range(1,N+1):
#         for j in range(1,i+1):
#             print(f'{arr[i][j]}', end=' ')
#         print()

# 다른 방법
# [2] 출력할 대상 값만 리스트로 만들어서 계산

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[1]*(i+1) for i in range(N)]

    for i in range(2,N):
        for j in range(1,i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

    print(f'#{tc}')
    for lst in arr:
        print(*lst)