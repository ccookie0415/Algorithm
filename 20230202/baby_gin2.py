import sys
sys.stdin = open('input_babygin.txt', 'r')
T= int(input())

def search_last(case):
    if case[0] == case[1]:
        if case[0] == case[2]:
            re=1
        else:
            re=0
    else:
        if int(case[0])+1 == int(case[1]) and int(case[0])+2 == int(case[2]):
            re=1
        else:
            re=0
    return re


for _ in range(T):
    case=list(input())
    case.sort()
    re=0
    for i in range(4):
        re = search_last(case[i:i+3])
        if re == 1:
            del case[i:i+3]
            re = search_last(case)
            break
    print(re)