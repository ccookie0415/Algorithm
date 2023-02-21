import sys
sys.stdin = open('input_ladder.txt', 'r')

def rotated(a):
  n = len(a)
  m = len(a[0])

  result = [[0]* n for _ in range(m)]

  for i in range(n):
    for j in range(m):
      result[j][n-i-1] = a[i][j]
  return result

T = int(input())
N = 100

for tc in range(1, T+1):
    arr = [list(map(int,input().split())) for _ in range(N)]

    row = 99
    col = 0

for j in range(N):
    if arr[99][j] == 2:
        col = j

while True:
    if arr[row][col] == 1:
        if arr[row][col+1] == 1:
            col += 1
        elif arr[row][col-1] == 1:
            col -= 1
        else:
            row += 1
    elif row == 0:
        print(col)
        break





