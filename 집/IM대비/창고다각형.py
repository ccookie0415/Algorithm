N = int(input())
lst = []
arr = [[0] * 1000 for _ in range(1000)]
#print(arr)

for _ in range(N):
    L,H = map(int,input().split())
    lst.append((L,H))

lst.sort()
print(lst)

for k in range(len(lst)-1):
    A = lst[k]
    B = lst[k+1]
    # if lst[k][1] > lst[k+1][1]:
    #     A,B=B,A
    print(A,B)
    # for i in range(lst[k+1][1])
    #     for j in range()






