# 마라톤에 참여한 선수들의 이름이 담긴 배열
# 완주한 선수들의 이름이 담긴배열
# 완주하지 못한 선수의 이름을 return

def solution(participant, completion):
    participant_dict = {}

    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict[p] = 1

    for c in completion:
        if c in participant_dict:
            participant_dict[c] -= 1

    for d in participant_dict:
        if participant_dict[d] == 1:
            return d
