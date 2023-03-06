N = int(input())
arr = [list(input()) for _ in range(N)]
max_ = 0

for i in range(N):
    for j in range(N-1):
        arr[i][j],arr[i][j+1] = arr[i][j+1],arr[i][j]
        for x in range(N):
            cnt = 1
            for y in range(N-1):
                if arr[x][y] == arr[x][y+1]:
                   cnt += 1
                   if max_ < cnt:
                       max_ = cnt
                else:
                    cnt = 1

        for y in range(N):
            cnt = 1
            for x in range(N-1):
                if arr[x][y] == arr[x+1][y]:
                    cnt += 1
                    if max_ < cnt:
                        max_ = cnt
                else:
                    cnt = 1

        arr[i][j], arr[i][j + 1] = arr[i][j + 1], arr[i][j]

for j in range(N):
    for i in range(N-1):
        arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]
        for x in range(N):
            cnt = 1
            for y in range(N-1):
                if arr[x][y] == arr[x][y+1]:
                   cnt += 1
                   if max_ < cnt:
                       max_ = cnt
                else:
                    cnt = 1

        for y in range(N):
            cnt = 1
            for x in range(N-1):
                if arr[x][y] == arr[x+1][y]:
                    cnt += 1
                    if max_ < cnt:
                        max_ = cnt
                else:
                    cnt = 1

        arr[i][j],arr[i+1][j] = arr[i+1][j],arr[i][j]


print(max_)

