N = int(input())
age_name_list = []
for i in range(0, N, 1):
    age, name = map(str, input().split())
    age = int(age)
    age_name_list.append([age, name])
# (key = lambda 인자 : 표현식)으로 x[0]인 age만 sort함수의 기준으로 삼게 만든다.
age_name_list.sort(key = lambda x : x[0])
for i in range(0, len(age_name_list), 1):
    print(age_name_list[i][0], age_name_list[i][1])