# f(i,k)    #i단계, k목표
# if i==k: 목표도달
# return
# else
# f(i+1,k) # 다음단계

def f(i,k):
    if i == k:
        print(B)
        return

    else:
        B[i] = A[i]
        f(i+1, k)


A = [10,20,30]
B = [0] * 3

f(0,3)