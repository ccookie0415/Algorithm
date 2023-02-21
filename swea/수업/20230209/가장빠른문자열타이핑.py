import sys
sys.stdin = open('input_가장빠른문자열타이핑.txt', 'r')

T = int(input())

for tc in range(1,T+1):
    sentence, target = input().split()
    sentence_ = sentence.replace(target, '0')
    ans = len(sentence_)

    print(f'#{tc} {ans}')