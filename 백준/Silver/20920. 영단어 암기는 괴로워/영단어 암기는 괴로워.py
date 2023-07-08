# 백준 20920번
# 자주 나오는 단어일수록 앞에 배치한다.
# 해당 단어의 길이가 길수록 앞에 배치한다.
# 알파벳 사전 순으로 앞에 있는 단어일수록 앞에 배치한다.
# 길이가 M 이상인 단어들을 외운다.
# 영어 지문에 나오는 단어의 개수 N, 외울 단어의 길이 기준이 되는 M
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
word_dict = {}
for i in range(0, N, 1):
    word = input().strip()
    if len(word) >= M:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
word_dict = sorted(word_dict.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))
for i in word_dict:
    print(i[0])