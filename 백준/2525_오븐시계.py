A,B = map(int,input().split())
C = int(input())

D = (A + (B+C)//60)%24
E = (B+C)%60

print(D,E)