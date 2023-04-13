# 매일 다른 옷을 조합하여 입어 자신을 위장함
# 서로 다른 옷의 조합의 수

def solution(clothes):
    answer = 1
    clothes_dict = {}

    for c in clothes:
        if c[1] in clothes_dict:
            clothes_dict[c[1]].append(c[0])
        else:
            clothes_dict[c[1]] = [c[0]]

    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    return answer - 1