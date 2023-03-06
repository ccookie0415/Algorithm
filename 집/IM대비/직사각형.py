N = 1
for _ in range(N):
    arr = [[0] * 301 for _ in range(301)]
    square_lst = []
    data = list(map(int,input().split()))
    square1 = data[:4]
    square2 = data[4:]
    square_lst.append(square1)
    square_lst.append(square2)

    for k in range(2):
        i1,j1,i2,j2 = square_lst[k][0],square_lst[k][1],square_lst[k][2],square_lst[k][3]
        for i in range(i1,i2+1):
            for j in range(j1,j2+1):
                arr[i][j] = arr[i][j] + k

    print(arr)