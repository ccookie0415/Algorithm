import sys
sys.stdin = open('3일차-string.txt', 'r', encoding = 'UTF-8')

T = 10

for tc in range(T):
    tc_num = int(input())
    target = input()
    sentence = input()
    result = 0
    for i in range(len(sentence)):
        if sentence[i] == target[0]:
            if sentence[i:i+len(target)] == target:
                result += 1
    print(f'#{tc_num} {result}')

