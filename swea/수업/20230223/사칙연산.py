import sys
sys.stdin = open('사칙연산.txt','r')

op = ['+','-','*','/']
def cal(node): #후위순회
    global result

    if not tree[node][0] in op:
        return tree[node][0]
    else:
        left = cal(tree[node][1])
        right = cal(tree[node][2])

        if tree[node][0] == '+':
            result = left + right
        elif tree[node][0] == '-':
            result = left - right
        elif tree[node][0] == '*':
            result = left * right
        elif tree[node][0] == '/':
            result = left // right

        return result

T = 10
for tc in range(1, T+1):
    N = int(input())
    tree = [[[] for _ in range(3)] for _ in range(N + 1)] #인덱스 1번부터 N번까지 사용하기 위함
    for i in range(N):
        node_info = input().split()
        node_num = int(node_info[0])
        node_data = node_info[1]
        if node_data not in op:
            tree[node_num][0] = int(node_data)
        else:
            tree[node_num][0] = node_data

        if len(node_info) == 4:
            tree[node_num][1] = int(node_info[2])
            tree[node_num][2] = int(node_info[3])

    result = 0
    cal(1)
    print(f'#{tc} {result}')




