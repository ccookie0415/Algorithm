N = int(input())
word_lst = dict()

for i in range(1,51):
    word_lst[i] = []

for j in range(N):
    word_ = input()
    word_lst[len(word_)].append(f'{word_}')

for k in range(1,51):
    word_lst[k].sort()

    for l in range(len(word_lst[k])):
        if l == 0 or word_lst[k][l] != word_lst[k][l-1]:
            print(word_lst[k][l])



n = int(input())
words = set()

for _ in range(n):
    words.add(input())
words = list(words)
words.sort(key=lambda x:(len(x), x))

for word in words:
    print(word)