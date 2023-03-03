cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
data = list(input())

for i in range(0,len(data)-2):
    if data[i]+data[i+1]+data[i+2] in cro:
        data[i]=data[i+1]=data[i+2] = '0'
        cnt += 1

for i in range(0,len(data)-1):
    if data[i]+data[i+1] in cro:
        data[i] = '0'
        data[i+1] = '0'
        cnt += 1

for i in data:
    if i != '0':
        cnt += 1

print(cnt)
