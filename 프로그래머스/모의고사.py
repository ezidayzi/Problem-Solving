def solution(answers):
    answer = []
    one = [1, 2, 3, 4, 5]
    two = [2, 1, 2, 3, 2, 4, 2, 5]
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    score = [0, 0, 0]
    for i, a in enumerate(answers):
        if one[i % len(one)] == a:
            score[0] += 1
        if two[i % len(two)] == a:
            score[1] += 1
        if three[i % len(three)] == a:
            score[2] += 1

    for i in range(len(score)):
        if score[i] == max(score):
            answer.append(i + 1)
    return answer