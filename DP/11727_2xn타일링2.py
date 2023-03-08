n = int(input())
square = [0,1,3]

for i in range(3,n+1):
    square.append(square[-1] + 2 * square[-2])

print(square[n] % 10007)