N = int(input())
arr = [list(input()) for _ in range(N)]
lst = ['C','P','Z','Y']
max_ = 0
ans=[]
di = [0,0,1]
dj = [1,-1,0]
di_2 = [1,-1,0]
dj_2 = [0,0,1]

for j in range(N):
    for i in range(N):
        if arr[i][j] in lst:
            cnt = 1
            while True:
                for l in range(1,N):
                    ni = i + l
                    nj = j
                    if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j]:
                        cnt += 1
                    elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != arr[i][j]:
                        for k in range(3):
                            ni_2 = ni+di[k]
                            nj_2 = nj+dj[k]
                            if 0 <= ni_2 < N and 0 <= nj_2 < N and arr[ni_2][nj_2] == arr[i][j]:
                                cnt += 1
                                break
                            else:
                                break
                else:
                    break
            ans.append(cnt)

# for i in range(N):
#     for j in range(N):
#         if arr[i][j] in lst:
#             cnt = 1
#             while True:
#                 for l in range(1,N):
#                     ni = i
#                     nj = j + l
#                     if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == arr[i][j]:
#                         cnt += 1
#                     elif 0 <= ni < N and 0 <= nj < N and arr[ni][nj] != arr[i][j]:
#                         for k in range(3):
#                             ni_2 = ni+di_2[k]
#                             nj_2 = nj+dj_2[k]
#                             if 0 <= ni_2 < N and 0 <= nj_2 < N and arr[ni_2][nj_2] == arr[i][j]:
#                                 cnt += 1
#                                 break
#                             else:
#                                 break
#                 else:
#                     break
#             ans.append(cnt)
# print(ans)
print(max(ans))
