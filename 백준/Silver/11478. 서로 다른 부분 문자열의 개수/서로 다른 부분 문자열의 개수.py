# 백준 11478번
S = input().strip()
answerlist = []
# S 문자열을 1글자씩, 2글자씩, 3글자씩, ... len(S) 글자씩 끊기
for i in range(0, len(S), 1):
    for j in range(i+1, len(S)+1, 1):
        temp = S[i:j]
        answerlist.append(temp)
answerlist = set(answerlist)
print(len(answerlist))