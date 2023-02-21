bb = [55, 7, 78, 12, 42]
aa = 5


N = 5

def bubble_sort(a,N):
    for i in range(N-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a
print (bubble_sort(bb,aa))
