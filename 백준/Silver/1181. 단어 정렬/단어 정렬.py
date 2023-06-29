import sys
input = sys.stdin.readline
N = int(input())
word_list = []
answerlist = []
for i in range(0, N, 1):
    word = input().strip()
    if word not in word_list:
        word_list.append(word)
word_list.sort()

for j in range(1, 51, 1):
    for i in range(0, len(word_list), 1):
        if len(word_list[i]) == j:
            answerlist.append(word_list[i])
for i in range(0, len(answerlist), 1):
    print(answerlist[i])