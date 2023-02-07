import sys
sys.stdin = open('input_숫자배열회전.txt', 'r')

def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]

    arr_90 = rotated(arr)
    arr_180 = rotated(rotated(arr))
    arr_270 = rotated(rotated(rotated(arr)))

    print(f'#{tc}')
    for i in range(N):
        for j in range(N):
            print(arr_90[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_180[i][j], end='')
        print(end=' ')
        for j in range(N):
            print(arr_270[i][j], end='')
        print()

    # print(ans)