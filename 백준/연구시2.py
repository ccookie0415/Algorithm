# import copy
#
# def check(arr, i, j, visited):
#     global ans
#     global count
#
#     if arr[i][j] == 0 :
#         count += 1
#         check(arr, i + 1, j, visited)
#         check(arr, i - 1, j, visited)
#         check(arr, i, j+1, visited)
#         check(arr, i, j-1, visited)
#         visited[i][j] = 0
#
#     if ans < count:
#         ans = count
#
# N, M = list(map(int, input().split()))
# arr = [list(map(int,input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
#
# temp = []
# virus = []
# start_i = 0
# start_j = 0
# ans = 0
#
# for i in range(N):
#     for j in range(M):
#         if arr[i][j] == 0:
#             temp.append((i,j))
#         if arr[i][j] == 2:
#             virus.append((i,j))
#
# for i in range(len(temp)-2):
#     for j in range(i+1, len(temp)-1):
#         for k in range(j+1, len(temp)):
#             count = 0
#             arr[temp[i][0]][temp[i][1]] = 1
#             arr[temp[j][0]][temp[j][1]] = 1
#             arr[temp[k][0]][temp[k][1]] = 1
#             check(arr, start_i, start_j, visited)
#             arr[temp[i][0]][temp[i][1]] = 0
#             arr[temp[j][0]][temp[j][1]] = 0
#             arr[temp[k][0]][temp[k][1]] = 0
#
# print(virus)

