# def fibonacci(N):
#     if N == 0:
#         return 0
#     if N == 1:
#         return 1
#     else:
#         return fibonacci(N-1) + fibonacci(N-2)

n = int(input())
fibonacci = [0,1]

for i in range(n-1):
    fibonacci.append(fibonacci[-2] + fibonacci[-1])

print(fibonacci[-1])


