data = []

N = int(input())

for i in range(1,N+1):
    i = str(i)
    tmp = i.count('3')+i.count('6')+i.count('9')

    i = int(i)
    if tmp == 0:
        print(i,end=' ')
    else:
        print('-'*tmp,end=' ')


