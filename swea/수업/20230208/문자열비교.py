import sys
sys.stdin = open('input_문자열비교.txt', 'r')

T = int(input())

def BruteForce(p, t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i = i - j
            j = -1
        i = i + 1
        j = j + 1
    if j == M : return 1
    else : return 0

for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    M = len(str1)
    N = len(str2)

    print (f'#{tc} {BruteForce(str1,str2)}')

