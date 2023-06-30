# Chat GPT의 답
N = int(input())
xlist = list(map(int, input().split()))

# 중복을 제거한 좌표를 오름차순으로 정렬하여 리스트 생성
compressed_coords = sorted(set(xlist))

# 압축된 좌표의 인덱스를 저장하는 딕셔너리 생성
index_dict = {coord: i for i, coord in enumerate(compressed_coords)}

# 압축된 좌표 인덱스를 리스트로 생성
answerlist = [index_dict[x] for x in xlist]

print(*answerlist)
